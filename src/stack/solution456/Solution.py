class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_max_stack = []
        if not nums or len(nums) < 3:
            return False

        for num in nums:
            min = num
            if len(min_max_stack) > 0 and min_max_stack[-1][0] < min:
                min = min_max_stack[-1][0]
            while min_max_stack:
                top = min_max_stack.pop()
                if num <= top[0]:
                    min_max_stack.append(top)
                    break;
                elif num < top[1]:
                    return True
                else:
                    continue

            min_max_stack.append([min, num])

        return False


def test1():
    solution = Solution()
    print(solution.find132pattern([4, 1, 3, 2]))

def test2():
    solution = Solution()
    print(solution.find132pattern([1, 2, 3, 4]))

def test3():
    solution = Solution()
    print(solution.find132pattern([3, 1, 4, 2]))

def test4():
    solution = Solution()
    print(solution.find132pattern([-1, 3, 2, 0]))

def test5():
    solution = Solution()
    print(solution.find132pattern([1, 0, 1, -4, -3]))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()