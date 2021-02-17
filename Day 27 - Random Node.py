import random 

class Node: 
    def __init__(self, data): 
        self.data= data 
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None

    def printRandom(self): 
        if self.head is None: 
            return
        if self.head and not self.head.next: 
            print("Randomly selected key is %d" %(self.head.data)) 

        random.seed() 
 
        result = self.head.data 

        current = self.head.next
        n = 2
        while(current is not None):
            if (random.randrange(n) == 0 ): 
                result = current.data 

            current = current.next
            n += 1

        print("Randomly selected key is %d" %(result)) 

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
ll.printRandom() 
