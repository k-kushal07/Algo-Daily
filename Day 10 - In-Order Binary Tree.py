class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    def inorder(self, root):
        fin = []
        if root:
            fin = self.inorder(root.left)
            fin.append(root.data)
            fin = fin + self.inorder(root.right)
        return fin

root = Node(27)
root.insert(17)
root.insert(33)
root.insert(11)
root.insert(19)
root.insert(47)
root.insert(49)

print(root.inorder(root))
