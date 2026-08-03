#stack using DLL
#Time complexity: O(1) 
#Space complexity: O(n) 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
    
    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top.prev = new_node
            self.top = new_node
    
    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        self.top.prev = None
        return temp.data
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    