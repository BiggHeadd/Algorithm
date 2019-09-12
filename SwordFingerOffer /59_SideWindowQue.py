# -*- coding:utf-8 -*-
class Solution:
    def findMax(self, array, window):
        win = []
        maxNum = []
        for index, number in enumerate(array):
            if window > 0:
                win.append(number)
                window -= 1
            else:
                maxTmp = max(win)
                maxNum.append(maxTmp)
                win.pop(0)
                win.append(number)
            if index == len(array)-1:
                maxTmp = max(win)
                maxNum.append(maxTmp)
            print(array, win)
        return maxNum


if __name__ == "__main__":
    solution = Solution()
    array = [2, 3, 4, 2, 6, 2, 5, 1]
    window = 3
    result = solution.findMax(array, window)
    print(result)