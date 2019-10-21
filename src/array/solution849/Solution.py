class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        if not seats:
            return None

        dp = [0] * len(seats)
        cur = seats.index(1)
        # calculate from left
        for i in range(len(seats)):
            if seats[i] == 1:
                cur = i
            dp[i] = abs(i-cur)

        # calculate from right
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                cur = i
            dp[i] = min(abs(cur - i), dp[i])

        return max(dp)

def test1():
    solution = Solution()
    print(solution.maxDistToClosest([1,0,0,0,1,0,1]))

def test2():
    solution = Solution()
    print(solution.maxDistToClosest([0,1]))

if __name__ == '__main__':
    test1()