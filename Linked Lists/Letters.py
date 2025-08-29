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

    def size(self):
        count = 0 
        current = self.tail
        while current:
            count += 1
            current = current.next 
        return count 

    def search(self, letter):
        current = self.tail 
        index = 0 
        while current is not None: 
            if current.data == letter:
                print(f"Letter {letter} found at index {index}")
                return True
            current = current.next
            index += 1
        print("Letter not found")
        return False 
    
    def deleteNode(self, data):
        if self.tail == None:
            return
        current = self.tail
        prev = self.tail 
        while current:
            if current.data == data:
                if current ==self.tail:
                    self.tail = current.next 
                else:
                    prev.next = current.next 
                return True
            prev = current  
            current = current.next
        return False
    
    def clear(self):
        self.tail = None 
        print("list cleared")

alphabet_letters = Letters()
alphabet_letters.insert("A")  
alphabet_letters.insert("B") 
alphabet_letters.insert("C") 
alphabet_letters.insert("D") 
alphabet_letters.insert("E") 
alphabet_letters.insert("F") 
alphabet_letters.insertAtIndex("G", 1)  
alphabet_letters.insertAtIndex("H", 4)  
alphabet_letters.traverse() 

alphabet_letters.size()

alphabet_letters.search("C")
alphabet_letters.search("E")

print("linked list after removing a node")
alphabet_letters.deleteNode("B")
alphabet_letters.deleteNode("F")
alphabet_letters.traverse() 

alphabet_letters.clear()
