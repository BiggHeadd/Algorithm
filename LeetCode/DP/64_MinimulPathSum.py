def printdp(dp):
    for each in dp:
        print(each)
    print()


class Solution:
    def minPathSum(self, grid) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        for row in range(rows):
            for column in range(columns):
                if row == 0 and column == 0:
                    continue
                if row - 1 < 0:
                    grid[row][column] += grid[row][column - 1]
                elif column - 1 < 0:
                    grid[row][column] += grid[row - 1][column]
                else:
                    grid[row][column] = min(grid[row][column] + grid[row][column - 1],
                                            grid[row][column] + grid[row - 1][column])
        return grid[rows - 1][columns - 1]

if __name__ == "__main__":
    solution = Solution()
    input = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    answer = solution.minPathSum(input)
    print(answer)