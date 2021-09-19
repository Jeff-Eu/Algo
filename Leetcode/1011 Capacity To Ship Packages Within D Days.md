# 1011. Capacity To Ship Packages Within D Days

Q: A conveyor belt has packages that must be shipped from one port to another within D days.

The ith package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `D` days.

Example 1:

```
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
```

Example 2:

```
Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
```

Example 3:

```
Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
```

## Answer

注意這題有在範例中才註明，貨物的順序不可以改變，所以我起初誤解題意用 heap 輕鬆解是錯的：

```python
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        weights.sort(key=lambda x:-x)
        hp = []
        for w in weights:

            if len(hp) < D:
                heapq.heappush(hp, w)
            else:
                w2 = heapq.heappop(hp)
                heapq.heappush(hp, w2+w)

        out = 0
        while hp:
            out = heapq.heappop(hp)
        return out
```

確實理解題意後，後來我用排列組合的方式寫出暴力法，當然超時，不過寫出來也是一種成就。

```python
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def dfs(idx, cut, lmax):
            sm = 0
            if cut == D-1:# ! D==1
								for i in xrange(idx, size):
                    sm += weights[i]
                lmax = max(lmax, sm)
                amax[0] = min(lmax, amax[0])

            for i in xrange(idx, size):
                sm += weights[i]
                lmax = max(lmax, sm)
                dfs(i+1, cut+1, lmax)

        size = len(weights)
        amax = [float('inf')]
        dfs(0, 0, 0)
        return amax[0]
```

OK，其實這題有兩種不同優勢的最佳解，分別是二分法(Binary Search)+貪心，以及DP。

我對二分法的研究比較有興趣，搞了不少時間研究，終於找到 Pattern 可以使用，這應該能應付大部分的二分法問題。

1. 參考了許多文件，首先列出內容正確有價值的：
    - [Rosettacode - Binary search](https://rosettacode.org/wiki/Binary_search)
    - [Binary search algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm)
2. 還有內容不太正確，不過有被他的概念啟發到：
    - [Ultimate Binary Search Template. Solved many problems](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)
3. 還有一個Leetcode官方提供的，我實在不懂為何要寫得那麼複雜，唯一的好處是有提供許多二分法的題目XD：
    - [Leetcode - Binary Search](https://leetcode.com/explore/learn/card/binary-search/)

先說結論，目前刷題遇到的 Binary Search，應該(尚未驗證全部)都可以用以下三種pattern解 (參考上面1.的文件得來)：

1. 陣列無重覆值

```
BinarySearch(A[0..N-1], value) {
  low = 0
  high = N - 1
  while (low <= high) {
      mid = (low + high) / 2
      if (A[mid] > value)
          high = mid - 1
      else if (A[mid] < value)
          low = mid + 1
      else
          return mid
  }
  return not_found // value would be inserted at index "low"
}
```

 2.  陣列有重覆值，回傳重覆元素最左邊的 idx，若該值不存在，則回傳插入後的位置 (Lower Bound Inclusive Binary Search):

Binary Search for **Inclusive Lower Bound**:

```
function binary_search_leftmost(A, n, T):
    L := 0
    R := n // 注意不是n-1，所以會是R等於 L+n
    while L < R:
        m := floor((L + R) / 2)
        if A[m] >= T:
            R := m
        else:
            L := m + 1
    return L

// pass: 704 35 278 69 410 1011 374

--上面是改自 Wiki的；下面是 Rosettacode的------
BinarySearch_Left(A[0..N-1], value) {
  low = 0
  high = N - 1
  while (low <= high) {
      mid = (low + high) / 2
      if (A[mid] >= value)
          high = mid - 1
      else
          low = mid + 1
  }
  return low
}

// pass: 704 35 278 69 410 1011 374 153
// wait: 1760 1482 fff
```

 3.  陣列有重覆值，回傳重覆元素最右邊的"下一個元素"的 idx，若重覆值不存在，則回傳插入後的下一個位置 (Upper Bound Exclusive Binary Search):

Binary Search for **Enclusive Upper Bound**:

```
BinarySearch_Right(A[0..N-1], value) {
  low = 0
  high = N - 1
  while (low <= high) {
      mid = (low + high) / 2
      if (A[mid] > value)
          high = mid - 1
      else
          low = mid + 1
  }
  return low
}
```

- 這三種 pattern 都可以用來解下面兩題(都是值沒重覆)
    - [704. Binary Search](https://leetcode.com/problems/binary-search/)
    - [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

    但如果沒有選對Pattern，回傳值就會需要修改，而且容易改錯；有選對也"可能"需要小幅修改(尚未遇到)Pattern選擇的方法是看題目的規範，以及要的是什麼，題目若規範沒有重覆值，則必選 Pattern 1；題目若有重覆值，要的是lower bound，就選Pattern 2，要的是 upper bound就選 Pattern 3；不過，第三種 pattern 實戰中可能不實用，因為它的 upper bound是 exclusive，(若想修改成inclusive，不是減1就沒事，還要考慮其他boundary cases，但應該只要改 return的地方就好)，或是改用下面 inclusive版本(修改自wiki的ref)

Binary Search for **Inclusive Upper Bound**:

```
function binary_search_rightmost(A, n, T):
    L := 0
    R := n // 注意不是n-1，所以會是R等於 L+n
    while L < R:
        m := floor((L + R) / 2)
        if A[m] > T:
            R := m
        else:
            L := m + 1
    # 若輸入有重覆值時，回傳最右邊重覆值的idx
    # 若輸入沒有重覆值，R會是插入後的idx
    return R - 1

# passed: 33
```

![1011%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days%20eeae24f1d2554859ac3b20980dd162e1/1101.png](1011%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days%20eeae24f1d2554859ac3b20980dd162e1/1101.png)

對於所有的二分法問題，都可以用上面兩張圖來示意，其中 x軸就相當於 lo ~ hi 的範圍，也就是我們要求的值的範圍，它會有一個對應的函式 y = f(x)。注意，這裡 y 是 x 的函式，所以可能存在 a != b，使得 f(a) = f(b)，並且該函式是一個遞增或遞減函式。

> 定理：若 y = f(x) 是一個遞增或遞減函式，若給定 y = C(常數)，則可以用二分法求出 x ~= k，使得 f(k) ~= C。

上面左圖代表是遞增函式；右圖是遞減函式，上面介紹的三種 Pattern 的代碼都是假設函式是遞增函式，例如，Pattern 2之中的 `A[mid]` 就相當於一個 遞增函式 `f(x) = A[x]` 用 mid 代入，所以原型其實是 `f(mid) >= value`，以這個 Pattern 2而言，它可以找到value的 inclusive lower bound；但如果是一個遞減函式，一樣要求出 value的 inclusive lower bound 的話，很容易從圖形中就可以想到將 f(mid) >= value 換成 f(mid) <= value。

```
BinarySearch_Right(A[0..N-1], value) {
  low = 0
  high = N - 1
  while (low <= high) {
      mid = (low + high) / 2
      // f(mid) <= value: // 遞減函式
      if f(mid) >= value: // 遞增函式
          high = mid - 1
      else
          low = mid + 1
  }
  return low
}
```

同理，其他兩種 Pattern，若要套用在遞減函式，只需要先找到 f(x)那行，再將 f(x) 那行的大於/小於變相反即可。

[觀察]：另外從3種 Pattern裡，我們可以從 y=f(x) 的圖形或是代碼中，觀察到 x 軸上的 hi 跟 lo 有下面性質：

- hi 只會停住或往左邊移動
- lo 只會停住或往右邊移動

因此若題目想不出 f(x)，也可以從 lo 跟 hi 是否會分別往右及往左移動(或是不動)，來判斷是否存在二分法，若存在二分法，就必定存在一個 f(x)，只是這種題目不需要詳細將 y = f(x) 想出來，只要假設有 y = f(x) 存在就好，不是什麼題目都先想出 y = f(x) 再來解二分法就一定比較快，比如[33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) 跟[278. First Bad Version](https://leetcode.com/problems/first-bad-version/)，它們的 y = f(x)其實是像如下，也就是binary的，都跟 value 沒關係。

```
[F F F T T T T]
```

注意一個容易被混淆的地方，遇到不考慮 value 的 f(x) 問題時，如果要分別使用 Pattern 2 或 Pattern 3 來求 lower bound 及 upper bound 的話，寫在 `R := m` (upper end) 的條件式原本分別為 `A[m] > value` 及 `A[m] >= value` ，雖然兩者有等號的差異，但在 "不考慮value的 f(x) 問題" 的條件上，因為不考慮value，使用的 f(x)需另外設計，跟原本那兩個判斷式的等號無關。

像這種 binary 函式不用 value 是因為它的 y 只會發生在某位置才產生差異，就可以鎖定差異的地方；不像一般的函式要給 value才能去鎖定，所以，理論上題目可以問要鎖定 y的某一個地方，例如 y=D 是佔 x軸上最長段的最左邊的x位置。

> 解題技巧：若題目要用二分法解的話，觀察是否有 value 需要參考。

[推測]：所以理論上以本題而言，若給 weight要反推 D是不合理的，故不能用二分法，因為 x 不能當作 y 的函式 (同一個y值會對應不同的 x)。

### 用來解本題：

首先我們要觀察下面這個函式是否為遞增或遞減函式

```python
# x 代表選的重量
def fun(x):
    y = 0
    sum = 0
    for w in weights:
        sum += w
        if x >= sum:
            continue
        else:
            y += 1
            sum = w
    y += 1
    return y # y代表 天數
```

我們可以發現若 最小重量=x，天數=y，則 y 會是 x 的一個遞減函式 y=f(x)，該 f(x)可以使用二分法。

不過，這題的 f(x) 函式要擴展到更廣義的範圍，若定義 f(x) 代表 x 重量(和的max)，所允許的天數，那 f(x) 圖形會是如下 S 的區間，並且包含折線段，依照題目問題的問題，在給定 y ≤ D 的情況下，要求出 x 的最小值。 f(x) 在與 y≤D 交集範圍後，x 的最小值解就能收斂在黃黑色折線段交集部分的最左邊，這種問題就像以前高中學過的線性規畫問題。

![1011%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days%20eeae24f1d2554859ac3b20980dd162e1/2021-04-15_204940.png](1011%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days%20eeae24f1d2554859ac3b20980dd162e1/2021-04-15_204940.png)

再來，我們如果能驗證上面程式碼的 fun(x) 與上圖黃黑色折線段是等價的話，我們就能用 fun(x) 來作本題二分法的函式。

因此我們需要證明一個數學問題：

觀察上面程式碼中的 fun(x)，可以發現裡面是用 greedy 型態的演算法來求得 y，如果 f(x) 最下方的黃黑色折線段等價於 fun(x)，那 fun(x) 就可以用來當作二分法的解。

要證明上面的數學觀念，可使用反證法，先假定使用 fun(x) 的演算法得到的 y 天會是最小的天數，如果對於同一個 x，有另外存在一個分割天數 *y2 會比 y 天還少*，就代表 fun(x) 不是 f(x) ；

因為我有重要的事要先忙，等有空再把內容寫完整，先放上一張圖片證明的關鍵圖，幫助以後回想：

![1011%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days%20eeae24f1d2554859ac3b20980dd162e1/2021-04-17_221724.png](1011%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days%20eeae24f1d2554859ac3b20980dd162e1/2021-04-17_221724.png)

不過，我發現無論是從前面或從後面做 Greedy 圈選，程式都可以過，舉例:

```
2 2 1 4 1 3 1
若給定重量為 5
從前面開始圈： 2 2 1, 4 1, 3 1  ==> 三天
從後面開始圈：2 2, 1 4, 1 3 1  ==> 三天
```

這同樣可以用類似上面貼的那張圖來證明，從後面 Greedy 圈到前面的天數若為 y3 天，則不可能存在其他的 y 天會比 y3 還少，也就是說在 x 的情況下， y3 天是最小的，而因為 y 天也是最小的，因此 y3 = y。 

本題 Python 代碼：

```python
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
				# x 代表選的重量
				def fun(x):
            y = 0
            sum = 0
            for w in weights:
                sum += w
                if x >= sum:
                    continue
                else:
                    y += 1
                    sum = w
            y += 1
            return y # y代表天數

        lo = max(weights)
        hi = sum(weights)+1
        while lo < hi:
            mid = (lo+hi)//2
            if fun(mid) <= D:
                hi = mid
            else:
                lo = mid+1
        return lo
```

捷徑篇：因為題目要求的是 weight，而該值會落在數學的[lo, hi]區間，那關於題目該用lower bound 還是 upper bound？有個捷徑技巧，因為題目要求的是 least weight capacity，代表不是求一個值，也就只有Pattern 2 跟 Pattern 3；而要求 "least"，代表要用lower bound，為何？ 因為不管是遞增或遞減函式，求 least (x軸上盡量左邊的解) 就一定是 lower bound，也就是 Pattern 2；相反地，如果某種題目要求的是 most XXX，那就要用 upper bound。