# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0.0 and exponent < 0:
            return 0

        exponentAbs = exponent
        if exponent < 0:
            exponentAbs = -exponent

        result = self.powerWithExpAbsStack(base, exponentAbs)
        if exponent < 0:
            result = 1.0 / result
        return result


    def powerWithExpAbs(self, base, exponentAbs):
        result = 1
        for i in range(exponentAbs):
            result *= base
        return result

    def powerWithExpAbsStack(self, base, exponentAbs):
        if exponentAbs == 0:
            return 1
        if exponentAbs == 1:
            return base

        result = self.powerWithExpAbsStack(base, exponentAbs >> 1)
        result *= result
        if exponentAbs & 0x1 == 1:
            result /= base

        return result

if __name__ == "__main__":
    solution = Solution()
    base, exponent = 3, 3
    result = solution.powerWithExpAbs(base, exponent)
    print(result)