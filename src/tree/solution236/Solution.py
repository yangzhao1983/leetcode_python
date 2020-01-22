from src.tree.TreeNode import TreeNode

class Solution:
    def __init__(self):
        self.ancestor = {}

    def lowerCommonAncestor(self, root, p, q):
        self.ancestor[root] = None
        self.dft_tree(root)
        start_p = p
        ancestors = []
        while start_p:
            ancestors.append(start_p)
            start_p = self.ancestor[start_p]

        start_q = q
        while not (start_q in ancestors):
            start_q = self.ancestor[start_q]

        return start_q

    def dft_tree(self, root):
        if not root:
            return
        self.ancestor[root.left] = root
        self.ancestor[root.right] = root

        self.dft_tree(root.left)
        self.dft_tree(root.right)

def test1():
    solution = Solution()
    tn1 = TreeNode(3)
    tn11 = TreeNode(5)
    tn12 = TreeNode(1)
    tn111 = TreeNode(6)
    tn112 = TreeNode(2)
    tn1111 = TreeNode(7)
    tn1112 = TreeNode(4)
    tn121 = TreeNode(0)
    tn122 = TreeNode(8)
    tn1.left = tn11
    tn1.right = tn12
    tn12.left = tn121
    tn12.right = tn122
    tn11.left = tn111
    tn11.right = tn112
    tn112.left = tn1111
    tn112.right = tn1112
    print(solution.lowerCommonAncestor(tn1, tn11, tn12).val)

if __name__ == "__main__":
    test1()