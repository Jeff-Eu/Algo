# 290. Word Pattern

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`.

**Example 1:**

```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```

**Example 2:**

```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```

**Example 3:**

```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

**Example 4:**

```
Input: pattern = "abba", s = "dog dog dog dog"
Output: false
```

**Constraints:**

- `1 <= pattern.length <= 300`
- `pattern` contains only lower-case English letters.
- `1 <= s.length <= 3000`
- `s` contains only lower-case English letters and spaces `' '`.
- `s` **does not contain** any leading or trailing spaces.
- All the words in `s` are separated by a **single space**.

## Answer

```java
// Runtime: 1 ms, faster than 80.49% of Java online submissions for Word Pattern.
// Memory Usage: 36.9 MB, less than 64.94% of Java online submissions for Word Pattern.
class Solution {
    public boolean wordPattern(String pattern, String s) {
        
        HashMap<Character, String> mp = new HashMap<>(); // 左邊map到右邊
        HashMap<String, Character> mp2 = new HashMap<>(); // 右邊map到左邊
        
        String[] words = s.split(" ");
        
        if(pattern.length() != words.length)
            return false;
        
        // 檢查左邊mapping到右邊
        for(int i=0; i<pattern.length(); i++) {
            
            String word = mp.get(pattern.charAt(i));
            
            if(word == null) {

                mp.put(pattern.charAt(i), words[i]);
                
            }else if(!word.equals(words[i])) {
                return false;
            }
        }
        
        // 檢查右邊mapping到左邊
        for(int i=0; i<pattern.length(); i++) {
            
            Character c = mp2.get(words[i]);
            
            if(c == null) {

                mp2.put(words[i], pattern.charAt(i));
                
            }else if(!c.equals(pattern.charAt(i))) {
                
                return false;
            }
        }
        
        return true;
    }
}
```