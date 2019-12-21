from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # queue
        # if queue size < k, append nums[i] to tail, end update.
        # if queue size == k, get queue head, append it to ans.
        #   if head_index == start, remove head, append nums[i] to tail. start update, end update
        # when append nums[i], if nums[i] > tail, tail out,
        # start - end = size
        nums_queue = deque()
        start = 0
        ans=[]
        for i in range(len(nums)):
            while nums_queue and nums[i] > nums[nums_queue[len(nums_queue)-1]]:
                nums_queue.pop()
            nums_queue.append(i)
            size = i - start + 1
            if size == k:
                ans.append(nums[nums_queue[0]])
                if start == nums_queue[0]:
                    nums_queue.popleft()
                start += 1
        return ans

def test1():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    solution = Solution()
    ans = solution.maxSlidingWindow(nums, k)
    print(ans)
def test2():
    nums = [1,-1]
    k = 1
    solution = Solution()
    ans = solution.maxSlidingWindow(nums, k)
    print(ans)
if __name__ == "__main__":
    test2()