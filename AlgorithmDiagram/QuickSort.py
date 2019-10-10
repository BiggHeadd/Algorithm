# coding:utf-8

class QuickSort(object):
    def __init__(self):
        pass

    def sort(self, numbers):
        if len(numbers) < 2:
            return numbers

        pivot = numbers[0]
        less = [number for number in numbers[1:] if number < pivot]
        greater = [number for number in numbers[1:] if number > pivot]

        return self.sort(less) + [pivot] + greater


if __name__ == "__main__":
    quickSort = QuickSort()

    numbers = [10, 5, 2, 3]
    answer = quickSort.sort(numbers)
    print(answer)