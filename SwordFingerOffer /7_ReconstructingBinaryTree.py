# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre == None:
            return None
        else:
            root = TreeNode(pre[0])
            root.left = self.reConstructBinaryTree(pre[1: tin.index(pre[0])+1], tin[: tin.index(pre[0])])
            root.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1: ], tin[tin.index(pre[0])+1:])
        return root

    def printTree(self, node):
        if node == None:
            return
        print(node.val)
        self.printTree(node.left)
        self.printTree(node.right)


if __name__ == "__main__":
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    in_order = [4, 7, 2, 1, 5, 3, 8, 6]
    solution = Solution()
    treeOrigin = solution.reConstructBinaryTree(pre_order, in_order)
    solution.printTree(treeOrigin)