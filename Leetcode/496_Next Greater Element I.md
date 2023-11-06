# 496. Next Greater Element I
Q: The **next greater element** of some element `x` in an array is the **first greater** element that is **to the right** of `x` in the same array.

You are given two **distinct 0-indexed** integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the **next greater element** of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return _an array_ `ans` _of length_ `nums1.length` _such that_ `ans[i]` _is the **next greater element** as described above._

**Example 1:**

**Input:** nums1 = [4,1,2], nums2 = [1,3,4,2]
**Output:** [-1,3,-1]
**Explanation:** The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

**Example 2:**

**Input:** nums1 = [2,4], nums2 = [1,2,3,4]
**Output:** [3,-1]
**Explanation:** The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

**Constraints:**

-   `1 <= nums1.length <= nums2.length <= 1000`
-   `0 <= nums1[i], nums2[i] <= 104`
-   All integers in `nums1` and `nums2` are **unique**.
-   All the integers of `nums1` also appear in `nums2`.

**Follow up:** Could you find an `O(nums1.length + nums2.length)` solution?

## Answer

複刷 - 這裡的重要觀念是使用到 Monostack，忘記的話[這5分多鐘的影片](https://www.youtube.com/watch?v=Dq_ObZwTY_Q)有滿清楚的解釋，
需要注意的是影片一開始的說明是從左依序循訪到右，但這在實作上除了會需要原本的Stack，"可能"還會需要使用dictionary(亦稱作map)的key/value的輔助去分別儲存 原本list的值/greater的值，亦即 list[i]/ans[i]；但若是從後面循訪至前面，就可以只用 Stack作輔助，相對來說時間空間都可以再節省。
先來一個範例，
```txt
4 2 3 7 5 1 4 6
```
無論是從那個方向循訪，使用的都是decreasing monostack，所以只需要注意取值的時候作法會不同，若是從開始到結束的循訪，每個元素的greater元素就會是把它pop out的元素，像上面的例子就是 7把3,2,4都 pop out，所以7會是他們的greater元素；
若是從右到左循訪，每個元素的greater元素就會是stack pop完之後，最後要push之前在stack上的top元素，可以用上面的例子自行模擬即明白。

回歸本題，這裡的需求跟影片的情形有一點不同，但基本觀念一樣，使用到decreasing monostack。

```python 3
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        sz = len(nums2)
        
        mp = dict()
        stack = []
        gs = [-1]*sz # greater list
        
        for i in range(sz):
            mp[nums2[i]] = i
        
        for i in range(sz-1, -1, -1):
            while stack:
                if nums2[i] < stack[-1]:
                    gs[i] = stack[-1]
                    break
                else:
                    stack.pop()
                    
            stack.append(nums2[i])
            
        ans = []
        for v in nums1:
            ans.append(gs[mp[v]])

        return ans        
        
'''example for explaination

4 2 3 7 5 1 4 6 original list
7 3 7 - - 4 6 - greater list

stack
7 5 6 

'''
```

-------------------

Jeff's first approach (not optimum solution but passed)
```cpp
/*
Runtime: 16 ms, faster than 27.59% of C++ online submissions for Next Greater Element I.
Memory Usage: 9 MB, less than 15.84% of C++ online submissions for Next Greater Element I.

Example:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
*/
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
	// value, index
	map<int, int> mp;

	// T: O(sz2)  S: O(sz2)
	for (int i = 0; i < int(nums2.size()); i++) {
		mp[nums2[i]] = i;
	}

	// T: worst = O((sz1 + sz2)*sz1)
	vector<int> ans;
	for (int i = 0; i < int(nums1.size()); i++) {
		int idx = mp[nums1[i]];

		int v = -1;
		for (int j = idx+1; j < int(nums2.size()); j++) {
			if (nums2[j] > nums2[idx]) {
				v = nums2[j];
				break;
			}
		}
		ans.push_back(v);
	}
	return ans;
}
```


參考了Youtuber的解法 [Next Greater Element I - Leetcode 496 - Python](https://www.youtube.com/watch?v=68a1Dc_qVq4)，自己試寫一遍
```cpp
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {

	map<int, int> mp;
	for (int i = 0; i < int(nums1.size()); i++) {
		mp[nums1[i]] = i;
	}

	stack<int> st;
	vector<int> ans(int(nums1.size()), -1);
	// for (auto& a : ans) {
	// 	a = -1;
	// }

	for (auto& num : nums2) {

			while (st.empty() == false && st.top() < num) {
				ans[mp[st.top()]] = num;
                st.pop();
			}

			if (mp.find(num) != mp.end())
				st.push(num);
		}
	
	return ans;
}
```

後來看到論譠的寫法，理解之後自己也寫一遍
```cpp
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {

	map<int, int> mp;
    
    stack<int> st;
    for(int n: nums2) {
        
        
        while(st.size()>0 && st.top()<n) {
            mp[st.top()] = n;
            st.pop();
        }
        st.push(n);
    }
    
    vector<int> ans;
//     for(int i=0; i<nums1.size(); i++) {
        
//         if(mp.find(nums1[i]) != mp.end())
//             ans.push_back(mp[nums1[i]]);
//         else
//             ans.push_back(-1);
        
//     }
    
	// 下面是取代上面for更精簡的寫法
    for(int n: nums1) {
        
        // ans.push_back(mp.find(n) != mp.end()? mp[n]: -1);
		// 下面是取代上面更精簡的寫法，map.count(n)的用法
		// https://cplusplus.com/reference/map/map/count/
        ans.push_back(mp.count(n) ? mp[n] : -1);
    }
    
    
    return ans;
}
```

## Reference
Monotonic Stack 相關題型：
https://liuzhenglaichn.gitbook.io/algorithm/monotonic-stack

#Easy 