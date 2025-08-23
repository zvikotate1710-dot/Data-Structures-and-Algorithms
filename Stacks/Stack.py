class Node: 
    def __init__(self, data = None):
        self.data = data 
        self.next = None 

class Plates: 
    def __init__(self):
        self.top = None 

    def push(self, data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node 
        else:
            new_node.next = self.top
            self.top = new_node
        
    def peek(self):
        if self.top: 
            return self.top.data
        return None 
    
    def pop(self): 
        if self.top:
            data = self.top.data
            if self.top.next: 
                self.top = self.top.next 
            else: 
                self.top = None
            return data 
        
plates_obj = Plates()
plates_obj.push("orange plate")
plates_obj.push("black plate")
plates_obj.push("blue plate")

plates_obj.peek()
plates_obj.pop()
plates_obj.peek()


    