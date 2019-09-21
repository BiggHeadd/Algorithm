# coding: utf8
"""
单链表定义如下：
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
"""
import sys


class Solution(object):
    def removeDuplicates(self, head):
        """
        :type head: ListNode
        """
        # 在这里编写代码

        _ = int(sys.stdin.readline())
        line = sys.stdin.readline().strip()
        samples = list(map(int, line.split()))

        if _ < 1 or _ > 65535:
            pass
        else:
            collect_dict = {}
            answer = []
            pHead = ListNode(0)
            p = pHead
            for sample in samples:
                if sample not in collect_dict.keys():
                    collect_dict[sample] = 1
                else:
                    collect_dict[sample] += 1
                if collect_dict[sample] <= 2:
                    answer.append(sample)
                    node = ListNode(sample)
                    p.next = node
                    p = p.next

            head.next = pHead.next
            printString = ""
            p = head.val
            while p:
                printString += str(p.val) + " "
                p = p.next
            print(printString)