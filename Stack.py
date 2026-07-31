#stack basic code
#time complexity O(1)
#space complexity O(n)

def stack():
    def __int__(self):
        self.items= []

    def is_empty(self):
        return len(self.items)==0
    
    def push(self,i):
        self.items.append(i)

    def pop(self):
        if len(self.items)==0:
            return "Cannot pop. Stack is empty"
        x = self.items.pop()
        return x
    
    def top(self):
        if len(self.items)==0:
           return "Cannot return top, Stack is empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
stack= stack()
stack.push(67) 
stack.push(100)
print(f"stack content= {stack}")
print(f"popped item = {stack.pop()}")
print(f"top item after pop = {stack.top()}")       
print(f"stack i empyt = {stack.is_empty()}")
print(f"stack size = {stack.size()}")