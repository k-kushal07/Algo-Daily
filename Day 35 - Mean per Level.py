class TreeNode:
     def __init__(self, val=0, left=None, right=None):
            self.val = val
             self.left = left
             self.right = right
        
def averageOfLevels(self, root: TreeNode) -> List[float]:
    if root is None:
        return []
        
    this_level =[root]
    next_level = []
    result = []
    while this_level:
        total=0
        for n in this_level:
            total = total + n.val   
            if n.left is not None:
                next_level.append(n.left)
            if n.right is not None:
                next_level.append(n.right)
        print(total)
        result.append(total/ len(this_level)  )
            
        this_level = next_level
        next_level = []
            
    return result
