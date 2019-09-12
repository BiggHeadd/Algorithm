# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.result = []
        self.path = []
        self.theSum = 0


    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []

        self.findPath(root, expectNumber)
        return self.result

    def findPath(self, node, expectNumber):
        if not node:
            return []
        self.theSum += node.val
        self.path.append(node.val)
        isLeaf = node.left == None and node.right == None
        # print(self.path, self.theSum, self.theSum == expectNumber and isLeaf)
        if self.theSum == expectNumber and isLeaf:
            print(self.path, self.theSum)
            self.result.append(self.path)

        if node.left:
            self.findPath(node.left, expectNumber)
        if node.right:
            self.findPath(node.right, expectNumber)

        self.path.pop()
        self.theSum -= node.val

    def FindPath_right(self, root, expectNumber):
        if not root:
            return []
        tmp = []
        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        else:
            left = self.FindPath_right(root.left, expectNumber - root.val)
            right = self.FindPath_right(root.right, expectNumber - root.val)
            for item in left + right:
                tmp.append([root.val] + item)
        return tmp

if __name__ == "__main__":
    solution = Solution()
    node10 = TreeNode(10)
    node5 = TreeNode(5)
    node12 = TreeNode(12)
    node4 = TreeNode(4)
    node7 = TreeNode(7)

    node10.left = node5
    node10.right = node12
    node5.left = node4
    node5.right = node7


    result = solution.FindPath_right(node10, 22)
    print(result)