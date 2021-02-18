class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None

    def pairSwap(self): 
        temp = self.head 
        if temp is None: 
            return
        while(temp is not None and temp.next is not None): 
            if(temp.data == temp.next.data): 
                temp = temp.next.next
            else: 
                temp.data, temp.next.data = temp.next.data, temp.data 
                temp = temp.next.next

    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 

    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data) 
            temp = temp.next

ll = LinkedList() 
ll.push(5) 
ll.push(4) 
ll.push(3) 
ll.push(11) 
ll.push(27) 
ll.pairSwap() 
ll.printList()
