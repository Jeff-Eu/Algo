# 239. Sliding Window Maximum
Q: You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```
Example 2:
```
Input: nums = [1], k = 1
Output: [1]
```
Example 3:
```
Input: nums = [1,-1], k = 1
Output: [1,-1]
```
Example 4:
```
Input: nums = [9,11], k = 2
Output: [11]
```
Example 5:
```
Input: nums = [4,-2], k = 2
Output: [4]
```
## Answer
解法一，Heap：

除了暴力法外還有三種解法，目前已理解兩種, 參考了[力扣這裡的第一種解法-使用heap](https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/)，一天後重練花13分。


引述的其內容稍作修改：

對於本題而言，初始時，我們將數組`(nums[i], i)`的前ķ個元素放入優先隊列中。每當我們向右移動窗口時，我們就可以把一個新的元素放入優先隊列中，此時堆頂的元素就是堆中所有元素的最大值(假設是 max heap)。然而這個最大值可能並不在滑動窗口中，在這種情況下，這個值在數組數字中的位置出現在*滑動窗口左邊界的左側*。因此，當我們後續繼續向右移動窗口時，這個值就永遠不可能出現在滑動窗口中了，我們可以將其永久地從優先隊列中移除。

我們不斷地移除堆頂的元素，直到其確實出現在滑動窗口中。此時，堆頂元素就是滑動窗口中的最大值。


補充：代碼裡 heap(即 hp)的size並不一定等於滑動窗口的大小(即 k)，然而在一開始想這題時容易相信heap的size等於k，造成往後的思考都會錯誤而白費。實際上 heap 在這裡是一個被動的角色，它只記錄滑動窗口的最大值，但它的size卻可以比k大，當滑動窗口在移動時，它不會在意又被新增一個數值進去，就得馬上刪除原來滑動窗口最左邊的在heap的值；heap只在乎是否它最大值的index，不再是位在滑動窗口內，就會被動地去觸發，刪除掉最大值的index不是在滑動窗口內的，這動作會一直做下去直到不再被觸發，然後再取一次heap最大值的就是位在滑動窗口內了，至於它是否還有其他元素是在滑動窗口外的那不重要，因為那些都不是當下滑動窗口的最大值；換個說法，這裡heap的每個元素是 `(nums[i], i)`(假設是max heap)，每次元素取出來都會有 index i，我都去檢查 i 是不是在滑動視窗 k 個範圍內，沒有就刪掉，下一次視窗再往右移動也不會再用到那筆早就已經超過範圍被刪掉的元素了. 

心得：想像heap可用來計算一個size為k的小陣列的極值；當這個陣列動態開始左右無限擴張，我們也想計算連續視窗範圍內的極值，原本的小陣列就像滑動視窗一樣，一開始已經有heap計算過，再丟進給它新的元素，只要再一些簡單的計算就能再得到新視窗位置的極值。

Time: O(NlogN), N=len(nums)
```python
# Runtime: 1928 ms, faster than 26.58% of Python online submissions for Sliding Window Maximum.
# Memory Usage: 34.3 MB, less than 7.33% of Python online submissions for Sliding Window Maximum.
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(nums)
        hp = []
        for i in xrange(k):
            hp.append((-nums[i], i))
        # 上兩行亦可寫成 
        # hp = [(-nums[i], i) for i in xrange(k)]
        
        heapq.heapify(hp)
        ans = [-hp[0][0]]
        
        for i in xrange(k, size):
            heapq.heappush(hp, (-nums[i], i))
            while hp[0][1] <= i-k:
                heapq.heappop(hp)
            ans.append(-hp[0][0])
        return ans     
```

解法二，單調隊列：

第二種解法是使用 [Monotone Priority Queue](https://en.wikipedia.org/wiki/Monotone_priority_queue)，中文叫單調隊列，[這邊有不錯的解釋](https://kknews.cc/zh-tw/code/vmnab5q.html)，建議先看過再去理解上面力扣的第二種解法的"Code"(快速掃過解釋因為我覺得他的解釋不是很好)，如果想看動畫來驗證的話，可以[參考這個](https://leetcode-cn.com/problems/sliding-window-maximum/solution/zhe-hui-yi-miao-dong-bu-liao-liao-de-hua-7fy5/)。 

其實從Code看會比較容易明白，要先有個觀念，單調佇列(Monotone Priority Queue)是一種Priority Queue，是以由小到大或是由大到小排序，所以最左邊的都會是極值。

來研究下面寫的code，先看第一組for迴圈，在一開始視窗範圍k個的陣列，是用大至小的單調佇列(q)，每次囊括進新的`nums[i]`檢查，我們想要取最大的，因此保持讓q由大至小排序，要取最大的時候就是拿`q[0]`，其實在塞入`nums[i]`進q之前，要不要把q右邊比`nums[i]`小的pop()掉都沒差，甚至我們可以在不用pop的情況下，用 binary insect `nums[i]`進去q，但問題是insert進去後剩下的元素都要往後推，造成效率不見得比較好。如果在 while裡面的 pop()做最糟的情況，就是把k個元素都pop過一次，那總共是花 2k 的次數，在一開始k個的範圍裡，用暴力法求最大值只要比對 k次反爾更快一點。

接下來看第二段 for迴圈，這裡就會看到 deque的威力，當開始檢查新的元素進來時，依然仿照第一段for迴圈的做法，將後面比 `nums[i]`還小的都 pop掉，再將`nums[i]`丟進去，做法一模一樣，這段變成如下的code：
```python
        for i in range(k, size):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
			
            ans.append(nums[q[0]])
```
最後一行就是每次將新的最大值加入到ans的list之中。假設沒有做別的事，這段for迴圈做完加上第一段for總共最差就是做 2N的次數(其中 N=len(nums))，可能會想問，被pop掉的元素有沒有可能是之後加進來的最大值？答案是不可能，因為他們會被pop掉，勢必有比他們大的元素加進來，所以被pop掉的永不會是最大值。

不過最後要再加個小修飾，在for迴圈的倒數第二行插入下面的判斷
```python
            if q[0] <= i-k:
                q.popleft()
```

很熟悉，沒錯這就是解法一用來篩選掉滑動窗口外的最大值(注意，這裡的滑動窗口指的是題目的滑動窗口，我們的解法一跟解法二，反而都沒那麼像滑動窗口，所以如果一開始就在想*滑動窗口的解法*，可能容易被卡住)，最後取的`q[0]`就是目前視窗內的最大值。

一天後重練花了約12分，但是submit有遇到兩次錯誤，原因是不小心會被它的兩層巢狀陣列結構搞迷糊。

Time: O(N), N=len(nums)
```python
# Runtime: 1472 ms, faster than 96.50% of Python3 online submissions for Sliding Window Maximum.
# Memory Usage: 29.9 MB, less than 78.59% of Python3 online submissions for Sliding Window Maximum.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        size = len(nums)
        for i in range(k):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            
        ans = [nums[q[0]]]
        for i in range(k, size):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if q[0] <= i-k:
                q.popleft()
            ans.append(nums[q[0]])
            
        return ans
```

* 網友說有相關題：
    * [Medium 59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)：後來我去寫的解法效能很好，也沒用到這方法，所以沒再去研究兩者的關聯。
    * [Easy 155. Min Stack](https://leetcode.com/problems/min-stack/)


第三種解法是使用 Sparse Table，待研究...
* Ref:
	* [前面易懂後面沒看] https://cp-algorithms.com/data_structures/sparse-table.html
	* [看起來friendly] https://www.youtube.com/watch?v=c5O7E_PDO4U&t=8s
	* [影片做得好懂其實不然，但他有帶入泛型觀念] https://www.youtube.com/watch?v=uUatD9AudXo&t=410s
	* [勉勉強強] https://brilliant.org/wiki/sparse-table/
* 網友相關題:
    * [Medium 238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) 的解法二


## 進階問題
Q: Given a matrix and a window size k, output the max/min value in the 2D sliding window with a window size of k by k.

Example 1:
```
Input:
3 4 2 1
1 5 4 6
3 6 7 2
3 2 5 4

k = 2

Output:
1 2 1
1 4 2
2 2 2
```

Example 2:
```
Input:
[ 1 6 3 8]
[ 5 2 7 4]
[ 9 10 15 12]
[13 14 16 11]

k = 2

Output:
[1 2 3]
[2 2 4]
[9 10 11]
```

If we want the results composed of MAX values.

Example:
```
Matrix = 
[[5, 2, 7, 44, 12, 7],
[45, 44, 13, 4, 0, 34],
[5, 2, 7, 11, 16, 42],
[5, 23, 7, 0, 12, 7],
[15, 2, 3, 32, 8, 32]]

k = 3

Output:
[[45, 44, 44, 44],
[45, 44, 16, 42],
[23, 32, 32, 42]]
```
## 進階問題Answer

參考了 [stackoverflow 有人問的 Sliding window minimum/maximum in 2D](https://stackoverflow.com/questions/10732841/sliding-window-minimum-maximum-in-2d). 接著自己實作出來驗證，過程中還修正了幾次變成長寬不同，min/max都可判斷，真的要在25分內正確寫出來不太容易XD。

```python
import heapq
def findExtrem(mtx, w, isMax):

    # If not isMax would be isMin
	sign = -1 if isMax else 1

	out2d = []
	height = len(mtx)
	width = len(mtx[0])
    # Downgrade x coordinate (horizontal)
	for y in xrange(height):
		hp = []
		for i in xrange(w):
			hp.append((sign*mtx[y][i], i))
		heapq.heapify(hp)

		out = [sign*hp[0][0]]
		for i in xrange(w, width):
			heapq.heappush(hp, (sign*mtx[y][i], i))
			while hp[0][1] <= i-w:
				heapq.heappop(hp)
			out.append(sign*hp[0][0])

		out2d.append(out)

	mtx = out2d
	out2d_t = []
	width = len(mtx[0])
	height = len(mtx)
    # Downgrade y coordinate (vertical)
	for x in xrange(width):
		hp = []
		for i in xrange(w):
			hp.append((sign*mtx[i][x], i))
		heapq.heapify(hp)

		out = [sign*hp[0][0]]
		for i in xrange(w, height):
			heapq.heappush(hp, (sign*mtx[i][x], i))
			while hp[0][1] <= i-w:
				heapq.heappop(hp)
			out.append(sign*hp[0][0])

		out2d_t.append(out)

	# Transpose out2d_t to out2d.
    # Note:
    #   1. 其實這步驟是為了上面 Downgrade y 軸 的代碼而設計的，上面的代碼為了寫起來跟 Downgrade x 軸差不多，所以存進 out2d_t 是一列一列存(否則應該要一排排存)，故還需要做一個 transpose 的動作才能變回真正結果。
    #   2. 先用 non-in-place 的做法，如果長寬相同，要做 in-place 很簡單，但若長寬不同，這問題就很難，可參考: https://stackoverflow.com/questions/9227747/in-place-transposition-of-a-matrix。
	height = len(out2d_t[0])
	out2d = [[0 for _ in xrange(width)] for _ in xrange(height)]
	for i in xrange(height):
		for j in xrange(width):
			out2d[i][j] = out2d_t[j][i]

	return out2d

#--------- Test cases -----------
mtx = \
[[3, 4, 2, 1],
[1, 5, 4, 6,],
[3, 6, 7, 2,],
[3, 2, 5, 4]]

print findExtrem(mtx, 2, False)

mtx = \
[[1, 6, 3, 8],
[ 5, 2, 7, 4],
[ 9, 10, 15, 12],
[13, 14, 16, 11]]

print findExtrem(mtx, 2, False)

mtx = [
[5, 2, 7, 44, 12, 7],
[45, 44, 13, 4, 0, 34],
[5, 2, 7, 11, 16, 42],
[5, 23, 7, 0, 12, 7],
[15, 2, 3, 32, 8, 32],
]

print findExtrem(mtx, 3, True)
```

### Archived 

承上進階題，以下是一開始的錯誤解法，代碼又長，掉入了陷阱XD。

簡單來說，我這裡的作法就是讓 heap 中是 window 範圍外位置的 item 都 pop 出去，但其實 window 移動到下一列(row)時，會用到一開始 window 重疊的範圍值，但這時候 heap 內已經找不到那些值了，所以就錯了。
```python
def findMin(mtx, w):
	
	hp = []
	n = len(mtx)
	for i in xrange(w):
		for j in xrange(w):
			hp.append((mtx[i][j], i, j))
	heapq.heapify(hp)
	size2 = n-w+1
	ans = [[0 for _ in xrange(size2)] for _ in xrange(size2)]

	ans[0][0] = hp[0][0]
	# run row once
	for j in xrange(w, n):
		for k in xrange(w):
			heapq.heappush(hp, (mtx[k][j], k, j))
		while hp[0][2] <= j-w:
			heapq.heappop(hp)
		ans[0][j-w+1] = hp[0][0]

	for i in xrange(w, n):
		for k in xrange(w):
			heapq.heappush(hp, (mtx[i][k], i, k))
		while hp[0][1] <= i-w or hp[0][2] >= w:
			heapq.heappop(hp)
		ans[i-w+1][0] = hp[0][0]

		for j in xrange(w, n):
			heapq.heappush(hp, (mtx[i][j], i, j))
			while hp[0][1] <= i-w or hp[0][2] <= j-w or hp[0][2] > j:
				heapq.heappop(hp)
			ans[i-w+1][j-w+1] = hp[0][0]

	return ans

mtx = \
[[1, 6, 3, 8],
[ 5, 2, 7, 4],
[ 9, 10, 15, 12],
[13, 14, 16, 11]]

print findMin(mtx, 2)
'''
wrong output: [[1, 2, 3], [5, 7, 7], [9, 10, 11]]
'''
```