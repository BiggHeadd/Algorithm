# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return None
        if k not in data:
            return 0

        FirstIndex = self.GetFirstNumber(data, 0, len(data), k)
        LastIndex = self.GetLastNumber(data, 0, len(data), k)
        if LastIndex == FirstIndex:
            return 1
        else:
            return LastIndex - FirstIndex + 1

    def GetFirstNumber(self, data, start, end, k):
        if start > end:
            return -1

        middle = (start + end) // 2
        middleData = data[middle]
        if middle==0 or k == middleData and data[middle-1] != k:
            return middle
        elif k > middleData:
            start = middle + 1
        else:
            end = middle - 1

        return self.GetFirstNumber(data, start, end, k)

    def GetLastNumber(self, data, start, end, k):
        if start > end:
            return -1

        middle = (start + end) // 2
        middleData = data[middle]
        if middle == len(data) - 1 or middleData == k and data[middle + 1] != k:
            return middle
        elif middleData > k:
            end = middle - 1
        else:
            start = middle + 1

        return self.GetLastNumber(data, start, end, k)

if __name__ == "__main__":
    solution = Solution()
    data = [1, 2, 3, 3, 3, 3, 4, 5]
    k = 10
    result = solution.GetNumberOfK(data, k)
    print(result)