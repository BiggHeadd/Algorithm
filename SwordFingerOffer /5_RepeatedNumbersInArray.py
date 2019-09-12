# -*- coding: utf-8 -*-

def duplicate(array):
    if len(array) == 0:
        print("False")
        return False

    for i in array:
        if i < 0 or i > len(array) - 1:
            print("False")
            return False

    for i in array:
        if array.count(i) > 1:
            print("True: ", i)
            return True
    print("False")
    return False

def duplicate2(array):
    if len(array) == 0:
        print("False")
        return False

    for i in array:
        if i < 0 or i > len(array) - 1:
            print("False")
            return False

    array_dict = {}
    for i in range(len(array)):
        if array[i] in array_dict.keys():
            print("True: ", array[i])
            return True
        else:
            array_dict[array[i]] = array[i]
    print("False")
    return False

def duplicate3(array):
    if len(array) == 0:
        print("False")
        return False

    for i in array:
        if i < 0 or i > len(array) - 1:
            print("False")
            return False

    for i in range(len(array)):
        while array[i] != i:
            if array[i] == array[array[i]]:
                print("True: ", array[i])
                return True

            tmp = array[i]
            array[i] = array[array[i]]
            array[tmp] = tmp
    print("False")
    return False

if __name__ == "__main__":
    question1 = [2, 1, 3, 1, 7]
    question2 = [2, 4, 3, 1, 4]
    question3 = [2, 4, 2, 1, 4]
    question4 = [2, 1, 3, 0, 4]
    question5 = [2, 1, 3, 5, 7]
    question6 = []
    duplicate(question1)
    duplicate3(question2)
    duplicate3(question3)
    duplicate3(question4)
    duplicate3(question5)
    duplicate3(question6)