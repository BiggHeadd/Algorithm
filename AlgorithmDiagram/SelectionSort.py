# coding:utf-8

class SelectionSort(object):
    def __init__(self):
        pass

    def findsmallest(self, array):
        smallest = array[0]
        smallestIndex = 0
        for i in range(1, len(array)):
            if array[i] < smallest:
                smallestIndex = i
                smallest = array[i]
        return smallestIndex

    def sort(self, array):
        newArr = []
        for i in range(len(array)):
            smallest = self.findsmallest(array)
            newArr.append(array.pop(smallest))
        return newArr

if __name__ == "__main__":
    selectionSort = SelectionSort()
    answer = selectionSort.sort([1,4,3,2,5,8,7])
    print(answer)