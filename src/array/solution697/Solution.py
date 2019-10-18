class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        start = {}
        for i in range(len(nums)):
            if nums[i] in start:
                start[nums[i]].append(i)
            else:
                start[nums[i]] = [i]

        dup = 1
        min_len = 50000
        for num in start:
            if len(start[num]) >= dup:
                len_dup = start[num][-1] - start[num][0] + 1
                if len(start[num]) > dup:
                    min_len = len_dup
                else:
                    if len_dup < min_len:
                        min_len = len_dup
                dup = len(start[num])
        return min_len


def test():
    solution = Solution()
    print(solution.findShortestSubArray([1, 2, 2, 3, 1]))

def test1():
    solution = Solution()
    print(solution.findShortestSubArray([1,2,2,3,1,4,2]))

if __name__ == '__main__':
    test1()
    test()