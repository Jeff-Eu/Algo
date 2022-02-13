# Python Algorithm

## Binary Search
[bisect module](https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/)
```python
import bisect
# This function returns the position in the sorted list, where the num passed in argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the list, the right most position where element has to be inserted is returned. 
# 請注意並不會真的插入到arr而改變了arr
# 這跟 bisect.bisect(arr, num) 是一樣的
bisect.bisect_right(arr, num)

# bisect_right跟 _left的差異是:
# If the element is already present in the list, the left most position where element has to be inserted is returned. 
# 請注意並不會真的插入到arr而改變了arr
bisect.bisect_left(arr, num)
```

[Binary search insertion](https://stackoverflow.com/questions/8024571/insert-an-item-into-sorted-list-in-python)
```python
# python 2 & 3 are both available !
import bisect

bisect.insort(arr, item)
```
