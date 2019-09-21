class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        if not cost:
            return 0

        if len(cost) <= 2:
            return cost[-1]

        cost.append(0)
        dp = [cost[0], cost[1]]
        for step in range(2, len(cost)):
            dp.append(min(cost[step] + dp[step - 1], cost[step] + dp[step - 2]))
        return dp[-1]

if __name__ == "__main__":
    solution = Solution()
    answer = solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print(answer)