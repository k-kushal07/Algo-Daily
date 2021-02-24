class Node: 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
def deepestLeftLeafUtil(root, lvl, maxlvl, isLeft): 
    if root is None: 
        return
    if(isLeft is True): 
        if (root.left == None and root.right == None): 
            if lvl > maxlvl : 
                deepestLeftLeafUtil.ptr = root 
                maxlvl = lvl 
                return
 
    deepestLeftLeafUtil(root.left, lvl+1, maxlvl, True) 
    deepestLeftLeafUtil(root.right, lvl+1, maxlvl, False) 
def deepestLeftLeaf(root): 
    maxlvl = 0 
    deepestLeftLeafUtil.ptr = None
    deepestLeftLeafUtil(root, 0, maxlvl, False) 
    return deepestLeftLeafUtil.ptr 

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.right.left = Node(5) 
root.right.right = Node(6) 
root.right.left.right = Node(7) 
root.right.right.right = Node(8) 
root.right.left.right.left = Node(9) 
root.right.right.right.right= Node(10) 

result = deepestLeftLeaf(root) 
if result is None: 
    print("No leaf present in the given tree")
else: 
    print("The deepest left child is", result.val)
