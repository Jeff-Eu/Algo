# 1239. Maximum Length of a Concatenated String with Unique Characters

Given an array of strings `arr`. String `s` is a concatenation of a sub-sequence of `arr` which have **unique characters**.

Return *the maximum possible length* of `s`.

**Example 1:**

```
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
```

**Example 2:**

```
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
```

**Example 3:**

```
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
```

**Constraints:**

- `1 <= arr.length <= 16`
- `1 <= arr[i].length <= 26`
- `arr[i]` contains only lower case English letters.

## Answer

看過[這篇教的dfs解法後](https://www.youtube.com/watch?v=iGiTptPPUq8)過兩小時再刷約花8分鐘寫出，這題先用一般的dfs去解，再去學更快的 DP解(會用到什麼bitwise，尚未研究)

新技能：

- 判斷字串是否有重覆的快速寫法(雖然不快)

    ```python
    def isDup(path):
        return len(path) != len(set(path))
    ```

下面為dfs解。估計Time: O( N^2 )    因為 C(N, 2) = N*(N-1)

```python
# Runtime: 100 ms, faster than 68.32% of Python online submissions for Maximum Length of a Concatenated String with Unique Characters.
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        def isDup(path):
            return len(path) != len(set(path))
            
        def dfs(idx, path):
            if ans[0] < len(path):
                ans[0] = len(path)
            
            for i in xrange(idx, sz):
                path2 = arr[i]+path
                if not isDup(path2):
                    dfs(i+1, path2)
            
        sz = len(arr)
        ans = [0]
        dfs(0, "")
        return ans[0]
```

原影片教學後面試圖改進上面 isDup 的函式，但變更慢XD"，可能是只有python才會這樣，C++應該就不會。

以下比較其他方法的速度

```python
# 使用位元運算
# Runtime: 200 ms, faster than 19.31% of Python online submissions for Maximum Length of a Concatenated String with Unique Characters.
def isDup(path):
		curr = 0
	  for i, c in enumerate(path):
	      val = 1<<(ord(c)-ord('a')) # 注意 1<<0 會等於 1
	      if curr & val > 0:
	          return True
	      curr |= val
	  return False
```

```python
# Runtime: 144 ms, faster than 30.45% of Python online submissions for Maximum Length of a Concatenated String with Unique Characters.
def isDup(path):
    st = set()
    for c in path:
        if c in st:
          return True
        st.add(c)
    return False
```

目前看到其他快的解法都是屬於上面提到的位元運算的方法去改進 isDup()