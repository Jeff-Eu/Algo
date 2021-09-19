# Algorithm 演算法

## Array 陣列
### 中間往外對稱擴展的陣列特性

**Lemma1**：(從詳解中的java solution學來的)，在array中某個index i 會使得 i 加上某個長度L等於index j，亦即 i + L == j，那 j - L == i
```
array:  0 1 2 3 4 5 6 7 
        i <--- L --->
                    j
```
**Lemma2**:
若 L 為奇數，則 L/2 == (L-1)/2；若 L 為偶數，則 (L-1)/2 == L/2 - 1


**Theorem**：(從詳解中的java solution推理而來的)

如下圖，陣列中有一段長度是 L 的子陣列，定義i為：若L為奇數，i就是子陣列的中心位置，
若L為偶數，i會是子陣列中間偏左一位的位置，則該子陣列的起始位置 s 跟結束位置 e 分別為下式，可由 lemma1 跟 lemma2 證明而得到：
```
s = i - (L-1)/2
e = i + L/2

<------ L ------> 
0 0 0 0 0 0 0 0 0 0 0 0 0 0
s       i       e
```

## 排序
	- 高手重點整理
		- http://spaces.isu.edu.tw/upload/18833/3/web/sorting.htm
	- in place
		- 一個 in-place algorithm 是一種使用小的，固定數量的額外之空間來轉換資料的算法
		- 一個算法有時候會錯誤地被稱為原地算法，只因為它用它的輸出資料會覆蓋掉它的輸入資料
		- More broadly, in-place means that the algorithm does not use extra space for manipulating the input but may require a small though nonconstant extra space for its operation. Usually, this space is O(log n), though sometimes anything in o(n) is allowed. Note that space complexity also has varied choices in whether or not to count the index lengths as part of the space used.
		- Also, allocation and deallocation are often slow operations.
	- stable sort:
		- 如果鍵值相同之資料，在排序後相對位置與排序前相同時，稱穩定排序

## Binary Search (二分搜尋法)
	- 指的是去搜尋一個已排序的陣列，用二分法的方式，所以稱作 Binary search，跟樹沒關係。

## Binary Tree (二元樹)
	- 高手重點整理
		- from 師大 http://www.csie.ntnu.edu.tw/~u91029/BinaryTree.html
		- 上面連結的首頁，整理了許多資訊科學的文章
			- http://www.csie.ntnu.edu.tw/~u91029/index.html
	
	- 二元搜尋樹 (BST)
		* 最麻煩的是在刪除節點的第三種case - 該節點有兩個子樹，有一套標準程序最好記起來(不要看中文wiki的，寫的不精確有誤！);
			- 摘錄wiki: Broadly speaking, nodes with children are harder to delete. 
			As with all binary trees, a node's in-order successor is its right subtree's
				left-most child, and a node's in-order predecessor is the left subtree's
				right-most child. In either case, this node will have only one or no child
				at all. Delete it according to one of the two simpler cases above.
		* Ref
			- [Wiki] https://en.wikipedia.org/wiki/Binary_search_tree
			- [Youtube]
				- https://www.youtube.com/watch?v=a-53QSxovUA
				- https://www.youtube.com/watch?v=wcIRPqTR3Kc

* 要了解 heap 的資料結構，[可以參考這部影片](https://www.youtube.com/watch?v=HqPJF2L5h9U)
	* heap 是個 complete binary tree
	* min heap 是所有父結點會比子結點相同或還要小，但同高度的兄弟結點大小是不一定的
	* add (python是用 heapq.heappush(list, element))，複雜度為 O(1) ~ O(logN)，元素交換最多的次數等同樹高，交換方向為由下往上
	* delete (python是用 heapq.heappop(list)), 複雜度為 O(1) ~ O(logN)，更新方向為由上往下
	* heap 可以做出 priority queue
    * heap 雖然是樹的資料結構，但一般都是用陣列來表示，才有快速計算的作用
    * heap 的高度就是比較的次數，可用來計算時間複雜度
    * heapify 是將一個non-heap的陣列變成heap，也同義於build heap，只使用 O(n)的時間，比一個個insert總共需要 O(nlogn)的時間還要再快
		* [尚未研究] [為何 build heap (heapify) 是 O(n)？](https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity)
	* 參考692.題的解法，看比較函數是怎麼寫的
		```python
		import collections
		import heapq
		class Solution:
			# Time Complexity = O(n + nlogk)
			# Space Complexity = O(n)
			def topKFrequent(self, words, k):
				"""
				:type words: List[str]
				:type k: int
				:rtype: List[str]
				"""
				# O(n)
				count = collections.Counter(words)
				heap = []
				# O(nlogk)
				for key, value in count.items():
					heapq.heappush(heap, Word(value, key))
					if len(heap) > k:
						heapq.heappop(heap)
				res = []
				for _ in range(k):
					res.append(heapq.heappop(heap).word)
				return res[::-1]

		class Word:
			def __init__(self, freq, word):
				self.freq = freq
				self.word = word
			
			def __lt__(self, other):
				if self.freq == other.freq:
					return self.word > other.word
				return self.freq < other.freq
			
			def __eq__(self, other):
				return self.freq == other.freq and self.word == other.word
		```

## 圖論
	* 圖論的題目最好都是先把圖形的資料結構建立出來，否則就會像解 Dijkstra 最短路徑問題一樣，因為無圖形資料結構支援，造成無法再改善成更快速解的情形。
	* Dijkstra’s Shortest Path Algorithm
		* 教學影片 https://www.youtube.com/watch?v=pVfj6mxhdMw
			* 這影片後面說"點可以任意選，不一定要選最小"，這句是錯的，[這個人](https://www.youtube.com/watch?v=pVfj6mxhdMw&lc=UgyIhUiANCPgANqYUJF4AaABAg)有留言提到 It always needs to be the one with smallest known distance, it is not true that you can choose a vertex with any criteria you want.
			* 這影片後面的revised版本看不太懂，先忽略
		* 要證明這個演算法，首先將這演算法跟BFS做聯結想像，它可以說是BFS的廣義版，而且演算法算是一種DP，所以可以想像graph若從leaf擴張更多的點及路徑，並不會影響內層graph已經計算的結果；另外要注意下次選的點是從src到目前被擴張的點之中，路徑最短的點，再從該點去擴張相鄰點並更新相鄰點的路徑長。整體的證明純粹用文字很難解釋清楚，要搭配前面的教學動畫或圖形，在腦海裡勾畫出圖形，或是自己也照上面教學的圖形跟表格練習一次，就可以在腦海中證明。
			* Breadth-first search can be viewed as a special-case of Dijkstra's algorithm on unweighted graphs, where the priority queue degenerates into a FIFO queue. - from [Wiki](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).
		
## P, NP, NP-Complete 的解釋
	* [推薦] https://www.youtube.com/watch?v=u2DLlNQiPB4
	* https://www.ycc.idv.tw/algorithm-complexity-theory.html