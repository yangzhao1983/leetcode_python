from src.tree.TreeNode import TreeNode
class Solution:

    def __init__(self):
        self.p_array = []
        self.q_array = []

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        "rtype: bool
        """
        return self.compare_pre_order(p, q)

    def compare_pre_order(self, root_p, root_q):
        if not root_p and not root_q:
            return True
        elif not root_p or not root_q:
            return False

        if root_p.val != root_q.val:
            return False

        if not self.compare_pre_order(root_p.left, root_q.left):
            return False

        if not self.compare_pre_order(root_p.right, root_q.right):
            return False

        return True


def test1():
    solution = Solution()
    tn1 = None
    tn2 = None
    print(solution.isSameTree(tn1, tn2))

def test2():
    solution = Solution()
    tn1 = None
    tn21 = TreeNode(1)
    tn22 = TreeNode(2)
    tn21.left = tn22
    print(solution.isSameTree(tn1, tn21))

def test3():
    solution = Solution()
    tn1 = TreeNode(1)
    tn11 = TreeNode(2)
    tn12 = TreeNode(2)
    tn1.left = tn11
    tn1.right = tn12

    tn2 = TreeNode(1)
    tn21 = TreeNode(2)
    tn22 = TreeNode(2)
    tn2.left = tn21
    tn2.right = tn22

    print(solution.isSameTree(tn1, tn2))

if __name__ == '__main__':
    test1()
    test2()
    test3()