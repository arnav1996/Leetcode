/*


Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.


*/

class Solution(object):
    def isSymmetric(self, root):
         return root==None or self.isSym(root.left,root.right)
    
    def isSym(self,left,right):
        if left==None and right==None:
            return True
        if left==None or right==None:
            return False
        return left.val==right.val and self.isSym(left.right,right.left) and self.isSym(right.right,left.left)
