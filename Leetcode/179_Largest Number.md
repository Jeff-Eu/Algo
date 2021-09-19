# 179. Largest Number
Q: Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

 

Example 1:
```
Input: nums = [10,2]
Output: "210"
```
Example 2:
```
Input: nums = [3,30,34,5,9]
Output: "9534330"
```
Example 3:
```
Input: nums = [1]
Output: "1"
```
Example 4:
```
Input: nums = [10]
Output: "10"
```
## Answer
The explanation on Leetcode's solution is rough and terrible. The best approach to this problem needs math collary. 
First, look at [this theorem and proof](https://leetcode.com/problems/largest-number/discuss/291988/A-Proof-of-the-Concatenation-Comparator's-Transtivity). Let's name it theorem 1.

We will use the theorem 1 later.

Assume that a'b represents the concatenation of non-negative a and b.

If value1 = a'b'c'... follows the rule that makes,

a'b > b'c and b'c > c'd and ... so on, until the end.

By the theorem 1, we can conclude that c'..'m'... in value1 makes c'm' > m'c

If value1 is not the largest value, there must be some value m which makes

a'b'm'... > a'b'c'...

=> m'... > c'...
=> m'...c'... > c'...m'...

According the initial rule
m'...c'... means m'c' > c'm
