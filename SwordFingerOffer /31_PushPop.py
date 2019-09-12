# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []

        self.result = []
        path = []
        theSum = 0
        self.findPath(root, expectNumber, theSum, path)

        return self.result

    def findPath(self, node, expectNumber, theSum, path):
        theSum += node.val
        path.append(node.val)
        isLeaf = node.left == None and node.right == None
        if theSum == expectNumber and isLeaf:
            self.result.append(path)

        if node.left:
            self.findPath(node.left, expectNumber, theSum, path)
        if node.right:
            self.findPath(node.right, expectNumber, theSum, path)

        path.pop()


if __name__ == "__main__":
    solution = Solution()
    result = solution.IsPopOrder([1,2,3,4,5], [4,5,3,2,1])
    print(result)