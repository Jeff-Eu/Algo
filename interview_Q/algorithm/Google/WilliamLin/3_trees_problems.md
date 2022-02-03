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