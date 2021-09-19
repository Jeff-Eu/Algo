# 583. Delete Operation for Two Strings
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
```
Input: "sea", "eat"
Output: 2
```
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
* The length of given words won't exceed 500.
* Characters in given words can only be lower-case letters.

## Answer

可以先看一遍詳解一直到 Method3，它所使用 lcs(s1, s2, m, n) (Longest Common Subsequence)中，m及 n這兩個參數分別代表 在s1上取前 m個字元的subsequence，及 s2上取前n個字元的subsequence，注意！是 subsequence 不是 substring；sequence是允許不連續的，string是連續的，這 lcs(s1, s2, m, n)就是回傳這兩個 subsequence的 longest common subsequence，接下再去看 lcs 這個函式的實作就容易懂。

詳解看到Method 2為止寫得還可以，但它是宣告 len+1 的長度，why？，理由是因為將字串長度 m, n當作函式的 input，但長度也有可能為 0，因此多記了一個，才會 len+1；像詳解寫 len+1 我覺得不易理解，改良成如下(改自Method 2)

```java
public class Solution {
    public int minDistance(String s1, String s2) {
        
        int[][] memo = new int[s1.length()][s2.length()];
        return s1.length() + s2.length() - 2 * lcs(s1, s2, s1.length()-1, s2.length()-1, memo);
    }
    public int lcs(String s1, String s2, int m, int n, int[][] memo) {
        if (m == -1 || n == -1)
            return 0;
        if (memo[m][n] > 0)
            return memo[m][n];
        if (s1.charAt(m) == s2.charAt(n))
            memo[m][n] = 1 + lcs(s1, s2, m - 1, n - 1, memo);
        else
            memo[m][n] = Math.max(lcs(s1, s2, m, n - 1, memo), lcs(s1, s2, m - 1, n, memo));
        return memo[m][n];
    }
}
```

Method 3, Using Longest Common Subsequence- Dynamic Programming

Method 2 是用 Top-Down 方式做遞迴的方法， Method 3，則是 bottom-Up的方式用 iteration(迭代)的方法，看了詳解的gif就比較容易懂，記得陣列宣告時，長寬也是要多加 1；我也有想過學上面 Method 2的改良法讓陣列的宣告不加1，但這會造成第一排及第一列的計算上稍微複雜一點(變成用很容易懂的方式直接比較，但code寫起來反而麻煩)，所以還是用詳解的方法，讓陣列的長寬多擴張一個cell，這樣在它程式裡的下面這片段仍然是合乎規則的。
```python
if (s1.charAt(i - 1) == s2.charAt(j - 1))
    dp[i][j] = 1 + dp[i - 1][j - 1];
else
    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
``` 

至於 Method 4 跟 Method 5 我是沒看，也不打算看懂，雖然 Method 5的空間複雜度可以縮減至 O(n)變成所有解法最好的，但其實看到詳解裡Method 3的 gif就可以想到，陣列的宣告可以縮減至 2 x Width，因為我們計算法只需要兩排就夠了，但寫起來會多一些 if-else的結構看起來會比較難懂。
