# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self):
        self.result = []

    def createList(self):
        head = pointer = ListNode(0)
        for i in range(1, 5):
            tmp_node = ListNode(i)
            pointer.next = tmp_node
            pointer = tmp_node
        self.head = head
        return head

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        result = []
        while listNode:
            result.append(listNode.val)
            listNode = listNode.next
        result.reverse()
        print(result)

    def printListFromTailToHead_recursion(self, listNode):
        if listNode:
            if listNode.next:
                self.printListFromTailToHead_recursion(listNode.next)

            # print("%d\t" %listNode.val)
            self.result.append(listNode.val)

        return self.result

if __name__ == "__main__":
    solution = Solution()
    list_node = solution.createList()
    solution.printListFromTailToHead(list_node)
    result = solution.printListFromTailToHead_recursion(list_node)
    print(result)