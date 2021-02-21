class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self): 
        self.head = None

    def prepend(self, data): 
        new_node = Node(data) 
        new_node.next = self.head 
        self.head = new_node 
 
    def insertAfter(self, prev, data): 
        if prev is None: 
            print("The given node doesn't exist.")
            return
        else:
            new_node = Node(data) 
            new_node.next = prev.next
            prev.next = new_node 

    def append(self, data): 
        new_node = Node(data) 
        if self.head is None: 
            self.head = new_node 
            return
        
        last = self.head 
        while (last.next): 
            last = last.next
        last.next = new_node 
 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data, end=' ') 
            temp = temp.next

llist = LinkedList() 
llist.append(1) 
llist.prepend(2) 
llist.prepend(3)
llist.append(4) 
llist.insertAfter(llist.head, 5) 
llist.printList() 
