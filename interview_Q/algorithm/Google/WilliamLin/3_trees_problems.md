https://www.youtube.com/watch?v=-tNMxwWSN_M

      1
     / \
    2   3
   / \ / \
  4  5 6  7
 / \
8   9 

Prompt #1. sum of depths for a node
```c++
int ans;
void dfs(Node u, int dep) {
	ans+=dep;
	if(u->left)
		dfs(u->left, dep+1)
	if(u->right)
		dfs(u->right, dep+1)
}
int sumDepths(Node root) {
	ans=0;
	dfs(root, 0);
	return ans;
}
```
Prompt #2. Sums of all depths of the subtrees in a binary tree
```c++
// p.first = number of nodes in subtree
// p.second = sum of depths in subtree
int ans;
pair<int, int> dfs(Node *u) {
	pair<int, int> p=make_pair(1, 0);

	if(u->left) {
		pair<int, int> pchild=dfs(u->left);
		p.second+=pchild.second+pchild.first;
		p.first+=pchild.first
	}
	if(u->right) {
		pair<int, int> pchild=dfs(u->right);
		p.second+=pchild.second+pchild.first;
		p.first+=pchild.first
	}
	ans += p.second;
	return p;
}

int sumDepths(Node *root) {
	ans=0;
	dfs(root);
	return ans;
}
```

Prompt #3. Sum of distances between the root node and the target node
```c++
// data sturcture:
// 	Node:(left, right, value (useless), number of nodes in each subtree)
//
// Example:
//       1
//      / \
//     2   3
//    / \ / \
//   4  5 6  7
//  / \
// 8   9 
//
// sumDists(2) = sumDists(1) - (number of nodes in subtree 2) + (number of nodes outside subtree 2)
// sumDists(5) = sumDists(2) - (number of nodes in subtree 5) + (number of nodes outside subtree 5)
// Formula:
// N = total number of nodes
// sumDists(u) = sumDists(parent(u))-size(u)+(n-size(u))

int ans, n;
pair<int, int> dfs1(Node *u) {
	pair<int, int> p=make_pair(1, 0);

	if(u->left) {
		pair<int, int> pchild=dfs(u->left);
		p.second+=pchild.second+pchild.first;
		p.first+=pchild.first
	}
	if(u->right) {
		pair<int, int> pchild=dfs(u->right);
		p.second+=pchild.second+pchild.first;
		p.first+=pchild.first
	}
	u->sz=p.first;
	return p;
}
void dfs2(Node *u, int sumDists, Node *target) {
	if(u==target)
		ans=sumDists;
	if(u->left) {
		int newSumDists=sumDists-(u->left->sz)+(n-u->left->sz);
		dfs2(u->left, newSumDists, target);
	}
	if(u->right) {
		int newSumDists=sumDists-(u->right->sz)+(n-u->right->sz);
		dfs2(u->right, newSumDists, target);
	}
}
//O(n) extra space
int sumDists(Node *root, Node *target) {
	pair<int, int> p=dfs1(root); //time: O(n)
	n=p.first;
	dfs2(root, p.second, target); //time: O(n)
	return ans;
}
```
Tracing...

      1
     / \
    2   3
   / \ / \
  4  5 6  7
 / \
8   9 

After calling dfs1:
n=p.first=9
sumDists(1)=p.second=16

dfs2(*1, 16, *4)
newSumDists=16-5+(9-5)=15
dfs2(*2, 15, *4)
newsumDists=15-3+(9-3)=18
dfs2(*4, 18, *4)

Time Complexity:
