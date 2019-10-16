class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)
        # cumulate from left
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]

        # cumulate from right
        cum_nums = 1
        for i in range(len(nums)-2, -1, -1):
            cum_nums *= nums[i+1]
            ans[i] *= cum_nums
        return ans

def test():
    nums = [1,2,3,4]
    solution = Solution()
    print(solution.productExceptSelf(nums))

if __name__ == '__main__':
    test()