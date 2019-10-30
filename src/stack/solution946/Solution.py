class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if not pushed or len(pushed) < 2:
            return True

        rel_stack = []
        popped_i = 0
        for pushed_item in pushed:
            rel_stack.append(pushed_item)
            while rel_stack and popped[popped_i] == rel_stack[-1]:
                popped_i += 1
                rel_stack.pop()

        return len(rel_stack)==0

def test1():
    solution = Solution()
    print(solution.validateStackSequences([1,2,3,4,5],[4,5,3,2,1]))

def test2():
    solution = Solution()
    print(solution.validateStackSequences([1,2,3,4,5],[4,3,5,1,2]))

if __name__ == '__main__':
    test1()
    test2()