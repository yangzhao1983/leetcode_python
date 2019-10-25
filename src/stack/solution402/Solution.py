class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # loop
        # if stack is empty, and cur_num is 0, continue, i++
        # if stack is not empty && cur_num < stack.peek && k>0, stack.pop, k--
        # else stack.push cur_num, i++
        i = 0
        num_list = []
        while i < len(num):
            if len(num_list) == 0 and num[i] == '0':
                i+=1
                continue
            elif len(num_list) > 0 and int(num[i]) < int(num_list[-1]) and k>0:
                num_list.pop()
                k-=1
            else:
                num_list.append(num[i])
                i+=1

        # loop until k ==0, stack is empty
        while k>0 and len(num_list) > 0:
            k -= 1
            num_list.pop()

        # if stack is empty, return '0'
        # else return stack to string
        if len(num_list)==0:
            return '0'
        else:
            return "".join(num_list)

def test1():
    solution = Solution()
    print(solution.removeKdigits('1432219',3))
def test2():
    solution = Solution()
    print(solution.removeKdigits('10200',1))
def test3():
    solution = Solution()
    print(solution.removeKdigits('10',2))
def test4():
    solution = Solution()
    print(solution.removeKdigits('9',1))
def test5():
    solution = Solution()
    print(solution.removeKdigits('112',1))

if __name__  == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()