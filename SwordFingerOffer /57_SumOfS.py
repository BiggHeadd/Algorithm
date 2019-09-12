# -*- coding:utf-8 -*-
class Solution:
    def findElement(self, array, target):
        if not array:
            return None
        head, tail = 0, len(array)-1
        while head != tail:
            theSum = array[head] + array[tail]
            if theSum == target:
                return [array[head], array[tail]]
            elif theSum > target:
                tail -= 1
            else:
                head += 1
        return None

if __name__ == "__main__":
    solution = Solution()
    array = [1, 2, 4, 7, 11, 15]
    target = 3
    result = solution.findElement(array, target)
    print(result)