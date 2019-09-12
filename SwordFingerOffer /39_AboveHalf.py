# -*-ccoding=utf-8 -*-

class Solution:
    def quick_sort(self, numbers):
        if len(numbers) < 2:
            return numbers

        middle = len(numbers) // 2
        left, right = [], []
        mid = numbers.pop(middle)
        for item in numbers:
            if item < mid:
                left.append(item)
            else:
                right.append(item)
        return self.quick_sort(left) + [mid] + self.quick_sort(right)

if __name__ == "__main__":
    numbers = [1,2,3,2,2,2,5,4,2]
    solution = Solution()
    result = solution.quick_sort(numbers)
    print(result)