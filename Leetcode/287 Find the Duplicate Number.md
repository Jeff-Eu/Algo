# 287. Find the Duplicate Number

Q: Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return _this repeated number_.

You must solve the problem by using only constant extra space.

Example 1:

```
Input: [1,3,4,2,2]
Output: 2
```

Example 2:

```
Input: [3,1,3,4,2]
Output: 3
```

**Constraints:**

- `2 <= n <= 3 * 10^4`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

## Answer

這題的相似題是 142. Linked List Cycle II，同樣可以使用 Floyd's cycle detection演算法去求得最佳解，這題的詳解用Floyd's演算法解說的還算清楚。

接下來我想用比較學術的方式講解這題，會導出一個猜想定理(因為沒有嚴謹證明才叫猜想)及一個新的演算法。

下圖是參考詳解的方法另外舉一個例子，注意到index 1以後元素的值都不會指向 index 0，而index 0的值因為從>0開始算(最小的可能是1)，所以只會指向後面的元素。若將陣列nums在graph中表示成，陣列中每個idx及其val(val等於`nums[idx]`)都代表node的ID，則在graph中，node idx會指向 node val。
![287%20Find%20the%20Duplicate%20Number%20639e11310e6042c4866c53b64f9440d0/287_1.png](287%20Find%20the%20Duplicate%20Number%20639e11310e6042c4866c53b64f9440d0/287_1.png)

**假設**：Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

**猜想定理：nums轉換成graph表示後，從node 0出發不斷指向下一個node，最後勢必會產生cycle。**

不專業證明:

![287%20Find%20the%20Duplicate%20Number%20639e11310e6042c4866c53b64f9440d0/287_2.png](287%20Find%20the%20Duplicate%20Number%20639e11310e6042c4866c53b64f9440d0/287_2.png)

```
參考上圖示意，不失其通用性。
將nums轉換成graph的步驟中，首先node 0會指向一個node u，而u這值會介落在1到n之間(已知nums的長度為 1+n，而nums的值只能填值是屬於{1...n})，接下來u指向的下一值v，只能指向值落在集合A = {1...n} - {u}，此時A會有 n-1個，否則u會指向前面的node，例如u本身，而產生cycle；而v指向的，勢必會落在集合 B = {1...n} - {u, v}，此時B會有 n-2個，否則會指向前面而產生cycle；因此，我們可推論從 0開始指向的值，若都不要產生cycle，那最多可以往前指向 n個元素，每個元素屬於集合{1...n}之中，並且彼此不相同。

而我們知道 1到n 就是nums從1以後的index，剛好這些index，{1...n}每個都已被指向(前一段的證明)，而此時graph最後一個node的數值代表於陣列中某一欄的index，但它要指向誰，亦即該欄的val要填誰，才不會產生cycle？現在集合裡面{1...n}都用過，沒得選，該欄位不能填新的值，只好填前面重覆過的，所以從graph看的話，它沒有新的值能指向，只能指向前面的node，這就是cycle。
```

觀察： 下面圖例可以觀察到，從index 0出發所指向的nodes中若存在某個node A被兩個以上別的node所指向，代表A就是重覆的數，這時我們很容易想到用Hash Set來找重覆值，但這需要O(N) 的空間。

![287%20Find%20the%20Duplicate%20Number%20639e11310e6042c4866c53b64f9440d0/287_1.png](287%20Find%20the%20Duplicate%20Number%20639e11310e6042c4866c53b64f9440d0/287_1.png)

我想到一種標記的演算法來解這題，但這標記演算法跟 [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) 的標記法不太一樣，但這兩種標記法有一個共同的重要觀念，*標記val 代表的是標記該val的 idx，亦即該 idx的node*，原因是idx是唯讀的不能被標記，特別要注意，這在程式的回傳值容易寫錯，下面兩個標記法最好是把圖形畫下來搭配著想，輔助對人腦做最有效率的思考。

我的標記法是從graph的node 0開始移動node，下一個node是它指向的，然後將每個尋訪過的node都做標記，標記的方式一樣是乘上-1，當發現有標記過的val就代表該index是重覆的值.

### Approach 1: Node指向尋訪標記法
Python
```python
# Runtime: 64 ms, faster than 76.99% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.5 MB, less than 77.89% of Python3 online submissions for Find the Duplicate Number.class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        pos = 0
        while True:
            if nums[pos] > 0:
                nums[pos] *= -1
                pos = -nums[pos]
            else:
                return pos # ATTENTION! not nums[pos]
        return -1
```

Kotlin
```java kotlin
class Solution {
    fun findDuplicate(nums: IntArray): Int {

        var pos = 0
        while (true) {
            if (nums[pos] > 0) {
                nums[pos] *= -1
                pos = -nums[pos]
            } else
                return pos
        }

        return -1
    }
}
```

接下來要介紹的是 [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)的標記法來解本題

### Approach 2: 陣列尋訪標記法

Python
```python
# Runtime: 48 ms, faster than 99.94% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.6 MB, less than 77.89% of Python3 online submissions for Find the Duplicate Number.class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for x in nums:
            ax = abs(x) # 注意這邊需取絕對值[註1]
            if nums[ax] > 0:
                nums[ax] *= -1
            else:
                return ax # ATTENTION! not nums[ax]

        return -1
```

註1：這個Approach一定要搭配 abs 的函式使用，如果不加abs下面例子就會出錯。建議畫圖並搭配舉例idx/val的陣列來理解。這裡我不好用寫的來輕鬆解釋，覺得拍影片解釋才比較清楚，有兩個關鍵思路如下：
- nums每一個元素的值都是標記在 idx 從 1 ~ (nums.size - 1)的元素上，當準備要標記已經被標記過的元素，就代表該 idx 就是重覆的值。
- 一開始 iterate 所有的 nums 可能會遇到負值，所以用 abs；巧妙的是，`nums[abs(x)]`才是上面那點一開始寫的想法，透過它遇到的負值才是代表被標記過的。

```
idx 0 1 2 3 4
val 1 3 4 2 2
```

Kotlin版本：
```java kotlin
class Solution {
    fun findDuplicate(nums: IntArray): Int {
        
        var idx = 0
		// for(v in nums) {
        //  idx = Math.abs(v)
        // 下面兩行也可以簡化成上面兩行：
		for(i in 0 until nums.size) {
            idx = Math.abs(nums[i])
            if(nums[idx] > 0)
                nums[idx] *= -1
            else
                return idx
        }
        return -1
    }
}
```

雖然本題若將陣列數字畫成graph，就會像上圖有個出發點node 0，並且在後面某個點開始形成cycle，造成至少有一個node被兩個不同node所指向的cycle，而 Floyd's algorthim 可以解這題。但事實上 Floyd's 演算法還能解從起點開始繞一圈回到起點的graph，這種 graph長得就像操場一樣，所以每個node都只被一個node所指向，這情況 Node標記法 跟 陣列標記法 都不能解決，只能依靠 Floyd's Algorithm。

### Approach 3: Floyd's Algorithm

另外詳解中有一個地方沒有說清楚，中間有導出一個公式

2d(tortoise)=d(hare), 亦即，龜走的距離的兩倍是兔走的距離

that means

(請配合看詳解中的圖)

2( F + a ) = F + nC + a, where n is some integer.

這裡有個地方沒有說清楚，為何第一次相遇的地方，是龜走 F + a？ 這意味著龜還沒有繞過一圈 C 之前就被兔相遇了，也就是這裡意味著

0 <= a <= (C-1) 其中 C 是環形長度有 n 個 node，

這個可以由國高中教的環形相遇問題的解法來證明，

因為兔速度是龜的2倍，因此

令 v(兔龜) 為 兔相對於龜的速度

v(兔龜) = (2-1)/次 = 1/次 (每次前進一個node)

假設環形有 n 個 node，一開始兔會先走，龜才會跟上，那等到龜走了 F 才開始進入環形的起始點，則不管這時候兔位於環形中那一個位置，龜在兔前面的距離 S (單位:node) 會滿足,

0 <= S <= n-1 (等於 0 時，代表兔龜相遇)

也就是說，從龜在進入環形起始點開始後，第一次龜兔相遇會在第 S/(2-1) = S 次的移動，這時候龜的位置從環形起始點算的話就是 S，也就是 a，

而因為 0 <= S <= n-1，所以第一次相遇的位置 a 不會超過一圈。

```python
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slw = fst = 0

        while True:
            slw = nums[slw]
            fst = nums[nums[fst]]
            if slw == fst:
                break

        slw = 0
        while True:
            fst = nums[fst]
            slw = nums[slw]
            if slw == fst:
                break

        return fst
```

```python
class Solution {
    fun findDuplicate(nums: IntArray): Int {

        var slw = 0
        var fst = 0

        do {
            slw = nums[slw]
            fst = nums[nums[fst]]
        } while(slw != fst)

        slw = 0
        while(fst != slw) {
            fst = nums[fst]
            slw = nums[slw]
        }
        return fst
    }
}
```

### Approach 4: 用位元組判斷重覆

```python
# Runtime: 84 ms, faster than 14.98% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.5 MB, less than 76.42% of Python3 online submissions for Find the Duplicate Number.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        curr = 0
        for i, v in enumerate(nums):
            val = 1<<v
            if curr & val > 0:
                return v
            curr |= val
```

### Other Notes

如果題目換成不是塞入1~n的整數，而是隨機的整數，就不能用上面提的演算法，我想到的是直接的暴力解：

```python
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        N = len(nums)
        while i < N-1:
            j = i+1
            while j < N:
                if nums[i] == nums[j]:
                    return nums[i]
                j+=1
            i+=1

        return None
```

## Relation
- Floyd's Algorithm -> [[142_Linked List Cycle II]]
- 標記演算法 -> [[442_Find All Duplicates in an Array]]


#medium