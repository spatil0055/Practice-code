class Node:
    def __init__(self,data):
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
    def insert_loop(self, pos):
        temp = self.head
        c = 1
        n = None
        while temp.next:
            if c == pos:
                n = temp
            temp =temp.next
            c += 1
        
        if n :
            temp.next = n
        else:
            print("Position out of range")
    
    def detect_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
    
    def get_length(self):
        temp = self.head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        return length

    def get_middle(self, l):
        mid = l // 2
        temp = self.head
        while temp and mid > 0:
            temp = temp.next
            mid -= 1
        return temp.data
    
    def reverse_list(self):
        prev = None
        next_node = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head =prev
    
    @staticmethod
    def merge_list(list1, list2):
        dummy = Node(-1)
        temp = dummy
        a = list1.head
        b = list2.head
        while a and b:
            if a.data < b.data:
                temp.next = a
                a = a.next
            else:
                temp.next = b 
                b = b.next
            temp = temp.next
        if a:
            temp.next = a
        if b:
            temp.next = b
        
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list
            
l1 = LinkedList()
l1.add(10)        
l1.add(20)        
l1.add(30)        
l1.add(40)        
l1.add(50)        
l1.display()

l2 = LinkedList()
l2.add(12)        
l2.add(45)        
l2.add(48)        
l2.add(51)
l2.display()

l3 = LinkedList.merge_list(l1,l2)
l3.display()
