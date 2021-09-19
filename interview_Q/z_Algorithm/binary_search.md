# Binary Search
### $ Concept
參考 Leetcode 1011的解說

### $ Cheat Sheet
* Pattern 1: 尋找value:
	```
	BinarySearch(A[0..N-1], value) {
	low = 0
	high = N - 1
	while (low <= high) {
		mid = (low + high) / 2
		if (A[mid] > value)
			high = mid - 1
		else if (A[mid] < value)
			low = mid + 1
		else
			return mid
	}
	return not_found // value would be inserted at index "low"
	}
	```

* Pattern 2: Binary Search for Inclusive Lower Bound:
	```
	function binary_search_leftmost(A, n, T):
		L := 0
		R := n // 注意不是n-1，所以會是R等於 L+n
		while L < R:
			m := floor((L + R) / 2)
			if A[m] >= T:
				R := m
			else:
				L := m + 1
		return L
	```
	或是  ------上面是改自 Wiki的；下面是 Rosettacode的，先記上面的就好------
	```
	BinarySearch_Left(A[0..N-1], value) {
	low = 0
	high = N - 1
	while (low <= high) {
		mid = (low + high) / 2
		if (A[mid] >= value)
			high = mid - 1
		else
			low = mid + 1
	}
	return low
	}
	```

* Pattern 3: Binary Search for Inclusive Upper Bound:
	```
	function binary_search_rightmost(A, n, T):
		L := 0
		R := n // 注意不是n-1，所以會是R等於 L+n
		while L < R:
			m := floor((L + R) / 2)
			if A[m] > T:
				R := m
			else:
				L := m + 1
		# 這是有重覆值時，回傳最右邊重覆值的idx
		# 若沒有重覆值，R會是插入後的idx
		return R - 1
	```
