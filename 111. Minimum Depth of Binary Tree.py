/*


Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.


*/

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.dfs(root)
    def dfs(self, root):
        if not root.left and not root.right:
            return 1
        elif not root.left:
            return 1 + self.dfs(root.right)
        elif not root.right:
            return 1 + self.dfs(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))      
