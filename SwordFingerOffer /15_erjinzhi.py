# -*- coding:utf-8 -*-
from ctypes import *
class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n).count('1') if n >= 0 else bin(2**32 + n).count('1')

    def NumberOf1_2(self, n):
        cnt = 0
        flag = 1
        while c_int(flag).value:
            if c_int(n & flag).value:
                cnt += 1
            flag = flag << 1
        return cnt

    def NumberOf1_3(self, n):
        cnt = 0
        while c_int(n).value:
            cnt+=1
            n = (n - 1) & n
        return cnt

    def expOf2(self, n):
        return True if bin(n & (n-1)).count("1") == 0 else False

if __name__ == "__main__":
    solution = Solution()
    question = 0
    result = solution.NumberOf1(question)
    result2 = solution.NumberOf1_2(question)
    result3 = solution.NumberOf1_3(question)
    print(result, result2, result3)

    result4 = solution.expOf2(3)
    print(result4)