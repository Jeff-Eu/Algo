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