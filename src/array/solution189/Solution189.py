class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if (not nums) or (len(nums) < 2):
            return

        k %= len(nums)

        if k==0:
            return

        count = 0
        start_pos = 0
        cur_pos = start_pos
        while count < len(nums):
            next_pos = (cur_pos + k) % len(nums)

            count += 1

            if next_pos == start_pos:
                start_pos+=1
                cur_pos = start_pos
            else:
                nums[start_pos], nums[next_pos] = nums[next_pos], nums[start_pos]
                cur_pos = next_pos
def main():
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    solution.rotate(nums, 3)
    print(nums)
    print('====')
if __name__ == '__main__':
    main()