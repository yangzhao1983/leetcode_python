class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack_nums = []
        stack_signs = []
        num_start = False

        for i in range(len(s)):
            # space
            if s[i] == ' ':
                continue
            # number
            if '0' <= s[i] <='9':
                num = int(s[i])
                if not num_start:
                    stack_nums.append(num)
                    num_start = True
                else:
                    high_num = stack_nums.pop()
                    stack_nums.append(high_num * 10 + num)
            else:
                num_start = False
                # ), pop up next sign, until (
                if s[i] == ')':
                    sign = stack_signs.pop()
                    if not sign == '(':
                        # calculate rel, and push it back to stack_num
                        stack_nums.append(self.cal_rel(sign, stack_nums))
                        stack_signs.pop()

                # (, push into stack
                elif s[i] == '(':
                    stack_signs.append(s[i])

                # +, -: pop up next sign if any, except (
                else:
                    if len(stack_signs) >0 and not stack_signs[-1] == '(':
                        # calculate rel, and push it back to stack_num
                        stack_nums.append(self.cal_rel(stack_signs.pop(), stack_nums))
                    stack_signs.append(s[i])

        if len(stack_signs) == 0:
            return stack_nums.pop()
        else:
            return self.cal_rel(stack_signs.pop(), stack_nums)

    def cal_rel(self, sign, nums):
        right = nums.pop()
        left = nums.pop()
        if sign == '-':
            return left - right
        else:
            return left + right

def test1():
    solution = Solution()
    print(solution.calculate('1 + 1'))

def test2():
    solution = Solution()
    print(solution.calculate('2-1+2'))

def test3():
    solution = Solution()
    print(solution.calculate('(1+(4+5+2)-3)+(6+8)'))

def test4():
    solution = Solution()
    print(solution.calculate('(1)'))

def test5():
    solution = Solution()
    print(solution.calculate('2147483647'))

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()