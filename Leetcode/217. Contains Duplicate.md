# 217. Contains Duplicate
Q: Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Example 1:**

**Input:** nums = [1,2,3,1]
**Output:** true

**Example 2:**

**Input:** nums = [1,2,3,4]
**Output:** false

**Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]
**Output:** true

**Constraints:**

-   `1 <= nums.length <= 105`
-   `-109 <= nums[i] <= 109`

## Answer

四種collections的c++寫法
```cpp
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;
bool containsDuplicate1(vector<int>& nums) {
	sort(nums.begin(), nums.end());
	for (int i = 0; i<int(nums.size()) - 1; i++) {
		if (nums[i] == nums[i + 1])
			return true;
	}
	return false;
}

bool containsDuplicate2(vector<int>& nums) {
	map<int, bool> myMap;
	// unordered_map<int, bool> myMap;
	for (auto& num : nums) {
		if (myMap.find(num) != myMap.end())
			return true;
		else
			myMap[num] = true;
	}
	return false;
}

bool containsDuplicate3(vector<int>& nums) {
	multimap<int, bool> myMap;
	// unordered_multimap<int, bool> myMap;
	for (auto& num : nums) {
		if (myMap.find(num) != myMap.end())
			return true;
		myMap.insert(make_pair(num, true));
	}
	return false;
}

bool containsDuplicate4(vector<int>& nums) {
	set<int> mySet;
	// unordered_set<int> mySet;
	// multiset<int> mySet;
	// unordered_multiset<int> mySet;
	for (auto& num : nums) {
		if (mySet.find(num) != mySet.end())
			return true;
		mySet.insert(num);
	}
	return false;
}

int main()
{
    std::cout << "Hello World!\n";

	int myints[] = { 32,71,33,45,26,80,53,33 };
	vector<int> myvector(myints, myints + 8);               // 32 71 12 45 26 80 53 33

	if (containsDuplicate4(myvector))
		cout << "true";
	else
		cout << "false";

	return 0;
}
```