# 416. Partition Equal Subset Sum
Q: Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:
```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```
Example 2:
```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```
## Answer

這題屬於01背包問題，

目前看到講解最清楚的是這兩個：
* Youtuber Bari 講解標準的 01背包問題：
    * 觀念: https://www.youtube.com/watch?v=nLmhmB6NzcM
        * 但例子應該舉項目的price依序是有大小穿插，而不是剛好都遞增，這樣會更好
    * 程式: https://www.youtube.com/watch?v=zRza99HPvkQ
		* 注意他程式為了方便說明，元素多插入一個0在首位。
* 官方講解本題：
    * https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/

邊邊知識可參考:
* https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/
* 他推薦很紅的背包九講(其實講的很簡略，覺得只有分類較好):
	* https://www.kancloud.cn/kancloud/pack/70125 

Bari在用程式講解 01背包問題時，dp的大小是用 (len(nums) + 1) x (target + 1)，也就是長寬各加 1，並且第一排跟列都為 0，這方式也可以應用在本題上，像官網跟其他論譠的解法大多是 len(nums) x (target + 1)，這時第一列就必須手動為boundary case填值，不能使用遞迴公式，這樣容易出錯，因此我將程式改為列也多加1，雖然效能差一點，但較不易出錯。

* 時間複雜度：O(NC)，這裡 N 是數組元素的個數，C 是數組元素的和的一半
    * 像上面這O(NC)是屬於"偽多項式時間"，因為它的 C 不是有數組的個數組成
    * [長知識] 偽多項式時間(Pseudo-polynomial time): From Wiki(英文定義比中文好) - A numeric algorithm runs in **pseudo-polynomial time** if its running time is a polynomial in the numeric value of the input (the largest integer present in the input)—but not necessarily in the length of the input (the number of bits required to represent it).

理解後的首刷(38分，多出25分主要在更正錯誤，跟官方首解有點不同，雖然多一排row，但實際寫發現有思路陷阱，在這程式後會說明):
```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        sm = sum(nums)
        if sm & 1 == 1:
            return False
        
        target = sm/2
        dp = [[False]*(target+1) for _ in xrange(size+1)]
        for i in xrange(size+1):
            dp[i][0] = True
            
        for i in xrange(1, size+1): # 易錯
            n = nums[i-1]  # 易錯
            for j in xrange(1, target+1):
                if j>=n:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-n]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[size][target]
        
'''reason

dp[i][j] = 
 dp[i-1][j], not pick idx i
 or dp[i-1][j-nums[i]], pick idx i

[0...i] index of nums
j is sum of picked ones

dp[i][0] = True
'''
```

上面是我多了一排首刷過的程式，雖然免去了第一排還要設 `dp[0][nums[0]] = True`，但發現在下面兩行易寫錯
```python
for i in xrange(1, size+1): # 易錯
    n = nums[i-1]  # 易錯
```
因為如果多了一排，`在dp[i][j]`裡的 i 意思就不是 index 在nums 從 0到 i；而是 index 在 nums 裡從 0到i-1，因為這時 i 的範圍會是 1到size，對應 nums 的index就必須是 i-1。
> 注意這問題也同樣發生在 Bari 講解01背包程式的地方，但他為了方便起見，將input最前面多塞了一個0進去，正如同下面截取網友的討論
```
Samiul Islam Ponik:
    k[i][w] = max(profit[i-1] + k[i -1][w - weight[i-1]], k[i-1][w]);

    Ahamed Kabeer:
        this logic applies when the first value of the weight array and profit array is not zero..Sir has made the first array elements as zero so the logic slightly changes..
```

不過，若真的堅持要寫的好看不易錯，有一種巧妙的方式可避開這易錯的寫法，就是下面改自官方解1的code，可以看到，同樣是多了一排，而且也不用設 `dp[0][nums[0]] = True`，但下面兩行仍是一樣的：
```python
for i in range(n):
    num = nums[i]
```
而且最後也是 `return dp[n - 1][target]`，這原理是，可以把它想成，我多了一排只是為了避開做 `dp[0][nums[0]] = True`，所以第一排初始化好之後，第二排即可用遞迴公式自動將 `dp[1][nums[0]]` 設為True(注意這裡變1不是0了)。但接著，我將第二排以後看成是將nums 的 0到 i對應到 `dp[i][j]`的 i，亦即符合原本dp轉移方程的定義，所以我最後也是回傳 `dp[n-1][target]`


官方第一解我改(註解部分是原本官網的)：
```python 3
# Runtime: 2124 ms, faster than 40.77% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 29.7 MB, less than 44.92% of Python3 online submissions for Partition Equal Subset Sum.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False
        
        target = total // 2
        if maxNum > target:
            return False
        
        # dp = [[0] * (target + 1) for _ in range(n)]
        dp = [[False] * (target + 1) for _ in range(n+1)]
        # for i in range(n):
        for i in range(n+1):
            dp[i][0] = True
        
        # dp[0][nums[0]] = True
        # for i in range(1, n):
        for i in range(n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n - 1][target] # 注意即使我使用不同於官方解而多了一排，但它還是返回 n-1 的理由
```

這也是為何官方解的第二個法，在第一個迴圈會是跑 len(nums) 次，因為它第一列參考的上一列其實就是多出來的，跟上面code的概念一樣，總共是用到 len(nums) + 1 列，多出來的第0列除了第一個值是True，其他每個值皆為 False。

另外這解法有一個不易理解之處，就是 dp[j- num]的下標難道不會是負值嗎？其實不會，因為 j 從target 遞減，所以若 j-num若為負值就不在 range的範圍內了，不會跑進去，這點比較抽象；想想如果是遞增的情況，超界就不會跑進迴圈中，同理遞減超界也是。

官方第二解：
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [True] + [False] * target # 注意第一欄還是皆為True
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1): # 也注意這裡要降序才不會用到改過的
                dp[j] |= dp[j - num]
        
        return dp[target]
```

初，超時解，dfs排列列舉法：
```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 超時解，約27分寫出
        # 後來再花幾分鐘加入 Memoization 但還是超時
        size = len(nums)
        ttl = sum(nums)
        nums.sort()
        mp = dict()
        def dfs(idx, sm, k):
            if k==0:
                if ttl == 2*sm:
                    # mp[(idx, sm, k)] = True
                    return True
            
            st = set()
            for i in xrange(idx, size):
                if nums[i] in st:
                    continue

                st.add(nums[i])
                if dfs(i+1, sm + nums[i], k-1):
                    # mp[(idx, sm, k)] = True
                    return True
                
            # mp[(idx, sm, k)] = False
            return False
        
        for i in xrange(1, size/2+1):
            if dfs(0, 0, i):
                return True
            
        return False
```