class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
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
        
    def delete(self, value):
        if not self.head:
            print("List empty")
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        
        while current and current.data != value:
            prev = current
            current = current.next
        
        if not current:
            print("Key not found")
            return
        prev.next = current.next
        
l1 = linked_list()
l1.add(10)
l1.add(20)
l1.add(200)
print("linked list")
l1.display()
l1.delete(20)
l1.display()

        