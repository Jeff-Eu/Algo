# 213. House Robber II
Q: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```
Example 2:
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```
Example 3:
```
Input: nums = [0]
Output: 0
``` 
## Answer
198. House Robber 的進階題

[拮取高手解的說明：](https://leetcode-cn.com/problems/house-robber-ii/solution/213-da-jia-jie-she-iidong-tai-gui-hua-jie-gou-hua-/)

环状排列意味着第一个房子和最后一个房子中只能选择一个偷窃，因此可以把此环状排列房间问题约化为两个单排排列房间子问题：
* 在不偷窃第一个房子的情况下（即 nums[1:]），最大金额是 p1；
* 在不偷窃最后一个房子的情况下（即 nums[:n−1]），最大金额是 p2 。
* 综合偷窃最大金额： 为以上两种情况的较大值，即 max(p1,p2) 。

```python
# Runtime: 16 ms, faster than 86.84% of Python online submissions for House Robber II.
# Memory Usage: 13.5 MB, less than 45.56% of Python online submissions for House Robber II.
class Solution:
    def rob(self, nums):
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]

```

直接從 198. House Robber 的解答 copy 過來修改的首刷 (200)
```python
# Runtime: 604 ms, faster than 6.41% of Python online submissions for House Robber II.
# Memory Usage: 13.6 MB, less than 15.13% of Python online submissions for House Robber II.
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        mem = {}
        def getMax(idx, fromFirst):
            if (idx, fromFirst) in mem:
                return mem[idx, fromFirst]
            
            # 注意2點，一開始一直寫錯 (注意邏輯，而非套招)
            # 1. 初始值 out跟 lm 不能設為 0
            out = lm = nums[idx]
            for i in xrange(idx, size):
                if fromFirst and i == size-1:
                    break
                for j in xrange(i+2, size):
                    if fromFirst and j == size-1:
                        break
                    lm = nums[i] + getMax(j, fromFirst)  # 2. 不能寫成 lm += getMax(j)，否則 lm 一直遞增上去
                    if lm > out:
                        out = lm
            mem[(idx, fromFirst)] = out
            return out
            
        amax = 0
        lmax = 0
        for i in xrange(size):
            lmax = getMax(i, i==0)
            if lmax > amax:
                amax = lmax
                
        return amax
```

2021/10/2 c++刷
```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int sz = nums.size();
        if(sz==1)
            return nums[0];
        else if(sz==2)
            return max(nums[0], nums[1]);
        else if(sz==3)
            return max(nums[0], max(nums[1], nums[2]));
        
        int ans = 0;
        // The first is selectable
        int pre2 = nums[0];
		// 注意這邊容易不小心寫錯
        int pre = max(nums[0], nums[1]);
        
        for(int i=2; i<sz-1; i++) {
            ans = max(pre2 + nums[i], pre);
            pre2 = pre;
            pre = ans;
        }
        
        int ans2 = 0;
        pre2 = nums[1];
		// 注意這邊容易不小心寫錯
        pre = max(nums[1], nums[2]);
        // The first isn't selectable
        for(int i=3; i<sz; i++) {
            ans2 = max(pre2 + nums[i], pre);
            pre2 = pre;
            pre = ans2;
        }
        return max(ans, ans2);
    }
};
```