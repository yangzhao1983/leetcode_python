class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_brackets = {'(':')','{':'}','[':']'}
        char_stack = []

        for i in range(len(s)):
            if s[i] in dict_brackets:
                char_stack.append(s[i])
            elif char_stack and dict_brackets[char_stack[-1]] == s[i]:
                char_stack.pop()
            else:
                return False

        return len(char_stack) == 0

def test1():
    solution = Solution()
    print(solution.isValid('()'))

def test2():
    solution = Solution()
    print(solution.isValid('()[]{}'))

def test3():
    solution = Solution()
    print(solution.isValid('(]'))

def test4():
    solution = Solution()
    print(solution.isValid('([)]'))

def test5():
    solution = Solution()
    print(solution.isValid('{[]}'))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
