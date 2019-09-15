# coding:utf-8
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray or len(rotateArray)==0:
            return 0

        head = 0
        tail = len(rotateArray)-1
        middle = head
        while head < tail:
            if (tail-head) == 1:
                middle = tail
                break
            middle = (head + tail) // 2
            if rotateArray[middle] >= rotateArray[head]:
                head = middle
            else:
                tail = middle
        return rotateArray[middle]