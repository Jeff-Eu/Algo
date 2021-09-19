# Q2. Permutation II
Q: Given "n" number of elements, please demonstrate how to output a permutation with a length of n.
(Duplications acceptable; please use only pseudo-code and/or algorithm in your answer.)

Input example: data = { 'a', 'b', 'c' }\
Output example: aaa, aab, aac, aba, abb, abc, ... , cca, ccb, ccc

My Answer:
```
Use n-based number system. In the system, we can map index i to data[i] in the array input, data.

If the length of permutation is 'm',
we can count the number from the smallest, zero, to the biggest, m numbers of (n-1).

```