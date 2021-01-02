class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def inOrder(self, root):
        res = []
        if root:
            res = self.inOrder(root.left)
            res.append(root.data)
            res = res + self.inOrder(root.right)
        return res

    def preOrder(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrder(root.left)
            res = res + self.preOrder(root.right)
        return res

    def postOrder(self,root):
        res = []
        if root:
            res = self.postOrder(root.left)
            res = res + self.postOrder(root.right)
            res.append(root.data)
        return res

root = TreeNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
# root.printTree()
print('inorder traversal:',root.inOrder(root))
print('preorder traversal:',root.preOrder(root))
print('postorder traversal:',root.postOrder(root))
