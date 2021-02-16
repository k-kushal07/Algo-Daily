class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def Intersect(self, headA, headB):
        c1 = headA 
        c2 = headB
        len1, len2 = 0

        while c1:
            len1 = len1 + 1
            c1 = c1.next
        while c2:
            len2 = len2 + 1
            c2 = c2.next

        if len1 > len2:
            for i in range(len1-len2):
                headA = headA.next
        
        else:
            for i in range(len2-len1):
                headB = headB.next
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
