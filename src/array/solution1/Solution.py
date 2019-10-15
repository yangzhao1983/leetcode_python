class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        left_to_index = {}
        for i in range(0, len(nums)):
            if nums[i] in left_to_index:
                ans.append(left_to_index[nums[i]])
                ans.append(i)
                break;
            else:
                left_to_index[target - nums[i]] = i

        return ans

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        left_to_index = {}
        for (offset, item) in enumerate(nums):
            if item in left_to_index:
                ans.append(left_to_index[item])
                ans.append(offset)
                break;
            else:
                left_to_index[target - item] = offset

        return ans