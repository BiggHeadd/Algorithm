# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return None

        numbers.sort()
        zeros = numbers.count(0)
        space = 0
        small = zeros
        big = small + 1
        print(numbers, zeros)
        while big < len(numbers):
            if numbers[small] == numbers[big]:
                return False
            space += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        if space <= zeros:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    result = solution.IsContinuous([1, 3, 2, 6, 4])
    print(result)