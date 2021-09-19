# 297. Serialize and Deserialize Binary Tree (Same with 449)
Q: Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:
```
    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
```
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

## Ans

跟 105題的解題觀念非常類似，這種用遞回traversal的過程，很難用描述來證明這做法是完全正確的(至少我目前想過的跟網路上都找不到)，但是有理解到一件事，traversal的細節仍需要用 stack，遞迴就是用stack來儲存當下的變數，並且樹的構建會是 bottom-up 上來(Back-tracking?)，也就是從葉子建構樹支，再把整棵樹建構起來，但中間的node會留在stack中等待連接起來




先參考Stefan高手的解如下，是使用preorder的方式。

不過要注意的是，若自己想嘗試變換，例如改用postorder，那根節點在字串的位置是在最後一個，deserialize時變成要從後面字串餵到前面來，而且不能像preorder的寫法跟serialize一樣的順序(preorder是: 值-左-右)，所以反而變得更麻煩(補充: postorder是bottom up的方式尋訪樹)；目前inorder也不知道該如何做XD。

其實比Stefan的解更好的方式是師大教學網站有提到的，preorder加inorder就可以用divide & conquer來得到一棵樹，不過有個條件是，節點的值不能有重覆，[如同Leetcode 105說明的](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)，所以除非這題有補充值不會重覆，否則並不適用；不過Stefan的做法雖然只有preorder，但是他有把樹的None點也寫進字串中，因此能夠讓時間跟空間都縮更短的解法應該是師大網站那方法。

另外論譠也有提到一些Level Order的解，但效率想見也不太會比preorder + inorder來得高(如果有非重覆的話)。

Stephan只有preorder就能deserialize成功的原因是它有把 None 記錄下來

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def doit(node):
            if node:
                lista.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                lista.append('#')
            
        lista = []
        doit(root)
        print ' '.join(lista)
        return ' '.join(lista)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def doit():
            v = next(it)
            if v == "#":
                return None
            node = TreeNode(v)
            node.left = doit()
            node.right = doit()
            return node
            
        it = iter(data.split())
        return doit()
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```