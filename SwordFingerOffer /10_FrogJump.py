# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2

        one, two, result = 1, 2, 0
        for i in range(2, number):
            result = one + two
            one = two
            two = result
        return result

    def rectCover(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        one, two, result = 1, 2, 0
        for i in range(2, number):
            result = one + two
            one = two
            two = result
        return result

if __name__ == "__main__":
    solution = Solution()
    result = solution.rectCover(2)
    print(result)