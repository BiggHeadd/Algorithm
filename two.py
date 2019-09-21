# coding: utf8
"""
单链表定义如下：
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
"""
import sys
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


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




        # collect_dict = {}
        # answer = []
        # while head:
        #     if head.val not in collect_dict.keys():
        #         collect_dict[head.val] = 1
        #     else:
        #         collect_dict[head.val] += 1
        #     if collect_dict[head.val] <= 2:
        #         # insert
        #         answer.append(head.val)
        #     head = head.next
        # printString = ""
        # for each in answer:
        #     printString += str(each) + " "
        # print(printString[:-1])

if __name__ == "__main__":
    solution = Solution()
    inputs = [2, 2, 1, 1, 1]
    head = ListNode(2)
    p = head

    for sample in inputs:
        node = ListNode(sample)
        p.next = node
        p = p.next
    solution.removeDuplicates(head)

    result = solution.head2
    while result:
        print(result.val)
        result = result.next