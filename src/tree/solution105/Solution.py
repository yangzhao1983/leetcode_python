from src.tree.TreeNode import TreeNode
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

    # 1. given an array representing a pre order traversal of a tree
    #    the left one is the root of the subtree
    # 2. given an array representing an inorder traversal of a tree
    #    nodes in the left sub array constitute the left sub tree
    #    nodes in the right sub array constitute the right sub tree
    def create_sub_tree(self, preorder, inorder):
        if not preorder:
            return None

        sub_tree_root_val = preorder[0]
        sub_tree_root = TreeNode(sub_tree_root_val)

        root_index = inorder.index(sub_tree_root_val)
        sub_tree_root.left = self.create_sub_tree(preorder[1:1 + root_index], inorder[0:root_index])
        sub_tree_root.right = self.create_sub_tree(preorder[1+root_index:], inorder[root_index+1:])

        return sub_tree_root

def test1():
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    solution = Solution()
    root = solution.create_sub_tree(preorder, inorder)
    print(root)

if __name__ == "__main__":
    test1()
