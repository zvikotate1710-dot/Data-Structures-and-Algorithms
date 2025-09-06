class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("None")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                current.next = current.next.next
                break
            current = current.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next
            count += 1 

'''
linked list for integers 
'''
print("Linked list for integers:")
ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.print() 
ll.insert_at_end(40)
ll.insert_at_end(50)
ll.print()
ll.insert_at(3, 25)
ll.insert_at(0, 5)
ll.print() 
ll.remove_at(2)
ll.print()
print("Length of linked list:", ll.get_length())
print(" ")

'''
linked list for strings
'''
print("Linked list for strings:")
ll.insert_values(["apple", "banana", "cherry"])
ll.print()
ll.insert_at(0, "orange")
ll.insert_at(2, "grape")
ll.insert_at(5, "kiwi")
ll.print()
ll.remove_at(1)
ll.print()
print("Length of linked list:", ll.get_length())