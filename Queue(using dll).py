#queue using DLL
# Time complexity: O(1) 
# Space complexity: O(n) 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        self.front.prev = None
        return temp.data
    
    def peek(self):
        if self.front is None:
            return None
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    