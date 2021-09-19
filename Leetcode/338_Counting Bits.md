# 338. Counting Bits
Q: Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:
```
Input: 2
Output: [0,1,1]
```
Example 2:
```
Input: 5
Output: [0,1,1,2,1,2]
```
Follow up:
* It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
* Space complexity should be O(n).
* Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

## Answer
雖然之前做過 191. Number of 1 bits ，就算用它的最佳解來應用在這題上，仍然不是這題的最佳解，請看[力扣高手提出來的解法](https://leetcode-cn.com/problems/counting-bits/solution/hen-qing-xi-de-si-lu-by-duadua/)

```python
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ls = [0]*(num+1)
        
        for i in xrange(1, num+1):
            if i % 2 == 1:
                ls[i] = ls[i-1] + 1
            else:
                ls[i] = ls[i/2]
                
        return ls
```

```java
class Solution {
    public int[] countBits(int n) {
        
//         int[] out = new int[n+1];

//         for(int i=0; i<n+1; i++) {
            
//             int c=0;
//             int j = i;
//             while(j!=0) {
//                 c++;
//                 j &= j-1;
//             }
//             out[i] = c;
//         }
                
//         return out;
        
        
        int[] out = new int[n+1];

        for(int i=0; i<n+1; i++) {
            int d = i/2;
            out[i] = out[d] + i%2; //(i%2==0) ? out[d] : out[d]+1;            
        }
                
        return out;
    }
}class Solution {
    public int[] countBits(int n) {
        
//// 使用 191. Number of 1 bits 的最佳解法，各別數字去算1的個數，但這方法在這題表現並不好
//         int[] out = new int[n+1];

//         for(int i=0; i<n+1; i++) {
            
//             int c=0;
//             int j = i;
//             while(j!=0) {
//                 c++;
//                 j &= j-1;
//             }
//             out[i] = c;
//         }
                
//         return out;
        
        // 這題最主要的作法，是利用每個數的 2的倍數的數，它們的 1的個數都會相同，因為只是將後面補上0
        int[] out = new int[n+1];

        for(int i=0; i<n+1; i++) { // 若將 n+1改成 n，並在前面先做 n+=1; 則速度從 42%上升到 99.9%
            int d = i/2; // 寫成 i>>1  速度從 28% 上升到 42%
            out[i] = out[d] + i%2; //(i%2==0) ? out[d] : out[d]+1;            
        }
                
        return out;
    }
}
```