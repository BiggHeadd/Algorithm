# coding:utf-8
class Fibonacci(object):
    def solution(self, n):
        if n<0:
            return 0

        result = [0, 1]
        if n<2:
            return result[n]

        pre = 1
        pre_two = 0
        now = 0
        for i in range(2, n+1):
            now = pre+pre_two
            pre, pre_two = now, pre
        return now

if __name__ == "__main__":
    fibonacci = Fibonacci()
    result = fibonacci.solution(0)
    print(result)