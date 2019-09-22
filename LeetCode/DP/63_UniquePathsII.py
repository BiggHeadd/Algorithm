
def printdp(dp):
    for each in dp:
        print(each)
    print()

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if not obstacleGrid:
            return 0

        rows, columns = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1 for _ in range(columns)] for _ in range(rows)]

        for row in range(rows):
            if obstacleGrid[row][0] == 1:
                for row_i in range(row, rows):
                    dp[row_i][0] = 0
                for column in range(columns):
                    dp[row][column] = 0
        for column in range(columns):
            if obstacleGrid[0][column] == 1:
                for column_i in range(column, columns):
                    dp[0][column_i] = 0
                for row in range(rows):
                    dp[row][column] = 0

        # printdp(dp)

        for row in range(1, rows):
            for column in range(1, columns):
                if obstacleGrid[row][column] == 1:
                    dp[row][column] = 0
                    continue
                dp[row][column] = dp[row - 1][column] + dp[row][column - 1]
        return dp[rows - 1][columns - 1]

    def uniquePathsWithObstacles_2(self, obstacleGrid) -> int:
        if not obstacleGrid:
            return 0

        obstacleGrid[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        rows, columns = len(obstacleGrid), len(obstacleGrid[0])
        for row in range(1, rows):
            if obstacleGrid[row][0] == 1:
                obstacleGrid[row][0] = 0
            else:
                obstacleGrid[row][0] = obstacleGrid[row - 1][0]
        for column in range(1, columns):
            if obstacleGrid[0][column] == 1:
                obstacleGrid[0][column] = 0
            else:
                obstacleGrid[0][column] = obstacleGrid[0][column - 1]

        # printdp(obstacleGrid)

        for row in range(1, rows):
            for column in range(1, columns):
                if obstacleGrid[row][column] == 1:
                    obstacleGrid[row][column] = 0
                else:
                    obstacleGrid[row][column] = obstacleGrid[row - 1][column] + obstacleGrid[row][column - 1]
        return obstacleGrid[rows - 1][columns - 1]


if __name__ == "__main__":
    solution = Solution()
    roads = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
    answer = solution.uniquePathsWithObstacles_2(roads)
    print(answer)