# 48. Rotate Image
Q: You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```
Example 2:
```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```
Example 3:
```
Input: matrix = [[1]]
Output: [[1]]
```
Example 4:
```
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
```
## Answer
* Leetcode 的詳解只有講用兩次鏡射會就可以做到，但沒有講為什麼，茲講解如下。

* 兩次的鏡射變換會合成一次的旋轉變換
	* ref: https://highscope.ch.ntu.edu.tw/wordpress/?p=51374
	* 觀念：旋轉角若為 2*(alpha-beta) 即等於，先對 beta 鏡射再對 alpha 鏡射 
	* 推移變換會改變幾何圖形的形狀，但不改變其面積
		* 線性變換的面積比
			* ref: http://highscope.ch.ntu.edu.tw/wordpress/?p=51317
			* 三角形面積公式 - 線性代數之 行列式 求三角形面積公式
				* ref: https://highscope.ch.ntu.edu.tw/wordpress/?p=66359

* 這題跟[[1041_Robot Bounded In Circle]]高度相關，1041題也有記錄一些值得學習的技巧可以去看看。

* 新技能：會寫此程式也能學會將一個矩陣的所有元素針對角線做鏡射的程式寫法
> 補充：有時候時間久了會忘記這個數學公式跟它的含意，甚至還會懷疑角度是要順時針還是逆時針，其實順逆時針在這題完全沒影響，記得不需擔心這點。  

* 看完詳解以及自己去找數學資料後首刷約 13分

```python
# Runtime: 20 ms, faster than 77.93% of Python online submissions for Rotate Image.
# Memory Usage: 13.3 MB, less than 73.59% of Python online submissions for Rotate Image.
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        # reflection on x=-y
        for i in xrange(size):
            for j in xrange(i, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # reflection on x=0
        for i in xrange(size):
            matrix[i].reverse()
```

二刷，
先對 0度映射，再對-45度映射

注意對 0度映射(x軸映射)及y軸映射的寫法，其實就是 reverse array的問題，這裡用到另一種不錯的寫法，不需要用到 `left+=1, right-=1, while(left<right)` 的作法，比較簡潔。
```python
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        arr = matrix
        h = len(matrix)
        w = len(matrix[0])
        
        for i in xrange(w):
            for j in xrange(h/2):
                arr[j][i], arr[h-j-1][i] = arr[h-j-1][i], arr[j][i]
                
        for i in xrange(h):
            for j in xrange(i):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

C++
速度贏過的比例不高，不過這方法類似詳解，還是可以接受的。
```cpp
// Runtime: 4 ms, faster than 54.69% of C++ online submissions for Rotate Image.
class Solution {
public:
    
    void rotate(vector<vector<int>>& matrix) {
        
        int sz = matrix.size();
        for(int i=0; i<sz-1; i++)
            for(int j=0; j<sz-i; j++)
                swap(matrix[i][j], matrix[sz-j-1][sz-i-1]);
        
        // int halfSz = sz/2; 
        // for(int i=0; i<halfSz; i++) {
        //     vector<int> tmp;
        //     tmp = matrix[i];
        //     matrix[i] = matrix[sz-i-1];
        //     matrix[sz-i-1] = tmp;
        // }
		// 下面這行的寫法可直接取代上面連續註解的那幾行
        reverse(matrix.begin(), matrix.end());
    }
};
```

#medium