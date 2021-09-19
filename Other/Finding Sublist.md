# Finding Sublist
From [How to test if a list contains another list?](https://stackoverflow.com/questions/3847386/how-to-test-if-a-list-contains-another-list)

How can I test if a list contains another list (ie. it's a contiguous subsequence). Say there was a function called contains:

```py
contains([1,2], [-1, 0, 1, 2]) # Returns [2, 3] (contains returns [start, end])
contains([1,3], [-1, 0, 1, 2]) # Returns False
contains([1, 2], [[1, 2], 3]) # Returns False
contains([[1, 2]], [[1, 2], 3]) # Returns [0, 0]
```

Edit:

```python
contains([2, 1], [-1, 0, 1, 2]) # Returns False
contains([-1, 1, 2], [-1, 0, 1, 2]) # Returns False
contains([0, 1, 2], [-1, 0, 1, 2]) # Returns [1, 3]
```



## Answer
Best answer, 

```python
def contains(small, big):
    for i in xrange(len(big)-len(small)+1):
        for j in xrange(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False
```

It returns a tuple of `(start, end+1)` since I think that is more pythonic, as Andrew Jaffe points out in his comment. It does not slice any sublists so should be reasonably efficient.

One point of interest for newbies is that it uses the [else clause on the for statement](http://docs.python.org/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) - this is not something I use very often but can be invaluable in situations like this.

This is identical to finding substrings in a string, so for large lists it may be more efficient to implement something like the [Boyer-Moore algorithm](http://en.wikipedia.org/wiki/Boyer_moore).

**Note:** If you are using Python3, change `xrange` to `range`.


## Learned
- Remember the art of the code.