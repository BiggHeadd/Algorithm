# -*- coding:utf-8 -*-
class node:
    def __init__(self, val, nextVal):
        self.val = val
        self.next = nextVal


class Solution:

    def LastRemaining_Solution(self, n, m):
        if n == 0 or m == 0:
            return -1
        numbers = [i for i in range(n)]
        step = m - 1
        begin = 0
        end = 0
        while len(numbers) > 1:
            end = (begin+step) % (n)
            # print(step, begin, end, n)
            numbers.pop(end)
            begin = end
            n-=1
        return numbers[0]


if __name__ == "__main__":
    solution = Solution()
    result = solution.LastRemaining_Solution(5, 3)
    print(result)