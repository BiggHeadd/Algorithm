# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if matrix == None or rows < 1 or cols < 1 or path == None:
            return False

        visited = [[False for col in range(cols)] for row in range(rows)]
        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        if pathLength == len(path):
            return True

        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row*cols+col] == path[pathLength] and not \
        visited[row][col]:
            pathLength += 1

            visited[row][col] = True

            hasPath = self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, visited) \
            or self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, visited) \
            or self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathLength, visited) \
            or self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, visited)

            if not hasPath:
                pathLength -= 1
                visited[row][col] = False

        return hasPath


    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0

        visited = [[False for col in range(cols)] for row in range(rows)]

        count = self.movingCountCore(threshold, rows, cols, 0, 0, visited)

        return count

    def movingCountCore(self, threshold, rows, cols, row, col, visited):
        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row][col] = True

            count = 1 + self.movingCountCore(threshold, rows, cols, row-1, col, visited)\
                      + self.movingCountCore(threshold, rows, cols, row, col-1, visited)\
                      + self.movingCountCore(threshold, rows, cols, row+1, col, visited)\
                      + self.movingCountCore(threshold, rows, cols, row, col+1, visited)


        return count

    def check(self, threshold, rows, cols, row, col, visited):
        if row>=0 and row<rows and col>=0 and col<cols and self.getDigit(row) + self.getDigit(col) <= threshold and not visited[row][col]:
            return True
        return False

    def getDigit(self, num):
        sum = 0
        while(num > 0):
            sum+=num%10
            num/=10
        return sum


if __name__ == "__main__":
    matrix = "ABCESFCSADEE"
    rows = 3
    cols = 4
    path = "ABCCED"
    visited = [[False for col in range(3)] for row in range(5)]
    solution = Solution()
    result = solution.hasPath(matrix, rows, cols, path)
    print(result)