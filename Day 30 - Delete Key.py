class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
 
    def append(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
            
    def deleteAllKey(self, key):
        temp = self.head
        prev = None
        
        while(temp!=None and temp.data==key):
            self.head = temp.next
            temp = self.head
            
        while(temp!=None):
            while(temp!=None and temp.data!=key):
                prev = temp
                temp = temp.next
            if(temp == None):
                return self.head
            prev.next = temp.next
            temp = prev.next
            
        return self.head
 
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end = ' ')
            curr = curr.next

llist = LinkedList()
n = int(input('Enter the number of elements: '))
for i in range(n):
    data = int(input('Enter the node value: '))
    llist.append(data)
key = int(input())
print('LinkedList: ', end = '')
llist.display()
print()
llist.deleteAllKey(key)
print('After deletion, LinkedList is: ')
llist.display()
