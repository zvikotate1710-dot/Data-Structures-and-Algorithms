class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class myStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

if __name__ == "__main__":
    stack = myStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print("Top element is:", stack.peek())  # Output: Top element is: 30
    
    print("Popped element is:", stack.pop())  # Output: Popped element is: 30
    print("Top element is:", stack.peek())  # Output: Top element is: 20
    
    print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False
    
    stack.pop()
    stack.pop()
    
    print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? True    