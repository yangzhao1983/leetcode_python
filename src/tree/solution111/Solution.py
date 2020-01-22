from src.tree.TreeNode import TreeNode

class Solution(object):
    def __init__(self):
        self.depth = 0

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.get_depth(root)

    def get_depth(self, root):
        if not root:
            return 0
        return 1 + min(self.get_depth(root.left), self.get_depth(root.right))


def test1():
    tn0 = TreeNode(3)
    tn01 = TreeNode(9)
    tn02 = TreeNode(20)
    tn021 = TreeNode(15)
    tn022 = TreeNode(7)
    tn0.left = tn01
    tn0.right = tn02
    tn02.left = tn021
    tn02.right = tn022
    solution = Solution()
    print(solution.get_depth(tn0))


def test2():
    tn0 = TreeNode(3)

    solution = Solution()
    print(solution.get_depth(tn0))


if __name__ == '__main__':
    test1()
    test2()
