class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, data):
        
        new = Node(data)
        
        if not self.head:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def insert(self, data, pos):
        c = 1
        n = Node(data)
        temp = self.head
        prev = None
        while temp and c < pos:
            prev = temp
            c += 1
            temp = temp.next
        if temp:
            n.next = prev.next
            prev.next = n
        else:
            print("position out of bound")
        
l1 = LinkedList()
l1.add(10)
l1.add(30)
l1.display()
l1.insert(20,2)
l1.display()
        