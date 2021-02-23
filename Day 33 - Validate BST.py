class newNode: 
    def __init__(self, key): 
        self.data = key 
        self.left = None
        self.right = None
def isBST(root, l = None, r = None): 
    if (root == None) : 
        return True
    if (l != None and root.data <= l.data) : 
        return False
    if (r != None and root.data >= r.data) : 
        return False
    return isBST(root.left, l, root) and isBST(root.right, root, r) 

root = newNode(1) 
root.left = newNode(2) 
root.right = newNode(4) 
root.right.left = newNode(5) 
root.right.right = newNode(6) 
root.right.left.left = newNode(47) 
if (isBST(root,None,None)): 
    print("Tree is BST.") 
else: 
    print("Tree is not a BST.") 
