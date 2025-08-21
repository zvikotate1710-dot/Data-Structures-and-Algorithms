class Node: 
    def __init__(self, data = None):
        self.data = data 
        self.next = None 

class Letters: 
    def __init__(self): 
        self.next = None
        self.tail = None

    def insert(self, data): 
        new_node = Node(data)

        if self.tail == None:
            self.tail = new_node
        else: 
            current = self.tail 
            while current.next is not None: 
                 current = current.next 
            current.next = new_node 
        
    def traverse(self): 
        current = self.tail  
        if current == None:
            print("There is nothing")
        else: 
            while current is not None: 
                print(current.data)
                current = current.next 
    
    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insert(data)
            return 
        position = 0 
        current = self.tail 
        while (current != None and position + 1 != index):
            position = position + 1 
            current = current.next 

        if current != None: 
            new_node = Node(data)
            new_node.next = current.next 
            current.next = new_node
        else:
            print("Index not present")

    def search(self, value):
        current = self.tail 
        index = 0 
        while current is not None: 
            if current.data == value:
                print(f"Value {value} found at index {index}")
                return True
            current = current.next
            index += 1
        print("Value not found")
        return False 

    def deleteFirstNode(self):
        if self.tail == None: 
            return
        self.tail = self.tail.next 

    def deleteNode(self, data):
        current = self.tail 
        if current.data == data: 
            self.deleteFirstNode()
            return
        while current is not None and current.next.data != data: 
            current = current.next 

        if current is None:
            return
        else:
            current.next = current.next.next 

    def clear(self):
        current = None
        self.tail = None 
        print("list cleared")

alphabet_letters = Letters()
alphabet_letters.insert("A")  
alphabet_letters.insert("B") 
alphabet_letters.insert("C") 
alphabet_letters.insertAtIndex("D", 1)  
alphabet_letters.traverse() 

alphabet_letters.search("D")

print("linked list after removing a node")
alphabet_letters.deleteNode("B")
alphabet_letters.traverse() 

alphabet_letters.clear()
