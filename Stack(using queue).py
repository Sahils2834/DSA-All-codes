#stack implementation using queue
#time complexity O(1)
#space complexity O(n)

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Underflow! Stack is empty."
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "No element to display! Stack is empty."
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Driver code
stack = Stack()

print(f"Is stack empty? {stack.is_empty()}")

stack.push(50)
stack.push(70)
stack.push(25)

print(f"Stack elements: {stack.items}")
print(f"Pop: {stack.pop()}")
print(f"Peek: {stack.peek()}")
print(f"Size of stack: {stack.size()}")
print(f"Is stack empty? {stack.is_empty()}")