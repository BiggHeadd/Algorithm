# -*- coding: utf-8 -*-

class Solution:
    def Find(self, target, array):
        found = False

        if array != [] and array != None:
            rows, columns = len(array), len(array[0])
            if rows > 0 and columns > 0:
                row = 0
                column = columns - 1
                while row < rows and column >= 0:
                    if array[row][column] == target:
                        found = True
                        break
                    elif array[row][column] > target:
                        column -= 1
                    else:
                        row += 1
        return found

if __name__ =="__main__":
    array1 = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    array2 = []
    solution = Solution()
    result = solution.Find(20, array1)
    print(result)