# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class PrintListFromTail(object):
    def __init__(self):
        self.result = []

    def reverse(self, listNode):
        if listNode:
            if listNode.next:
                self.reverse(listNode.next)
            self.result.append(listNode.val)

        return self.result

if __name__ == "__main__":
    a, b, c, d = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    printListFromTail = PrintListFromTail()
    answer = printListFromTail.reverse(a)
    print(answer)