# coding:utf-8
class Solution:
    def minimumTotal(self, triangle) -> int:
        if not triangle:
            return 0

        rows, columns = len(triangle), len(triangle[-1])
        dp = [[0 for _ in range(columns)] for _ in range(rows)]

        dp[0][0] = triangle[0][0]
        for row in range(rows):
            for column in range(row + 1):
                choice = 0
                if row - 1 >= 0 and column - 1 >= 0 and column < row:
                    dp[row][column] = min(dp[row - 1][column], dp[row - 1][column - 1]) + triangle[row][column]
                    choice=1
                elif row - 1 >= 0 and column - 1 >= 0:
                    dp[row][column] = dp[row - 1][column - 1] + triangle[row][column]
                    choice=2
                elif row - 1 >= 0:
                    dp[row][column] = dp[row - 1][column] + triangle[row][column]
                    choice=3
        return min(dp[-1])

    def minimumTotalOn(self, triangle) -> int:
        if not triangle:
            return 0

        rows, columns = len(triangle), len(triangle[-1])

        dp = triangle[-1]
        for row in range(rows-2, -1, -1):
            for column in range(row+1):
                dp[column] = min(dp[column], dp[column+1]) + triangle[row][column]
        return dp[0]

if __name__ == "__main__":
    solution = Solution()
    triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    answer = solution.minimumTotalOn(triangle)
    print(answer)