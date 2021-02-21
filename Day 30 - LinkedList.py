class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self): 
        self.head = None

    def prepend(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
 
    def insertAfter(self, prev_node, new_data): 
        if prev_node is None: 
            print("The given node doesn't exist.")
            return
        else:
            new_node = Node(new_data) 
            new_node.next = prev_node.next
            prev_node.next = new_node 

    def append(self, new_data): 
        new_node = Node(new_data) 
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
            print temp.data, 
            temp = temp.next

if __name__=='__main__': 
    llist = LinkedList() 
    llist.append(6) 
    llist.prepend(7) 
    llist.prepend(1); 

	# Insert 4 at the end. So linked list becomes 1->7->6->4->None 
	llist.append(4) 

	# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
	llist.insertAfter(llist.head.next, 8) 

	print 'Created linked list is:', 
	llist.printList() 

# This code is contributed by Manikantan Narasimhan 
