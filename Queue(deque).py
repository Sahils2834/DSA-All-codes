#doubly ended queue
#time complexity O(1)
#space complexity O(n)

class Deque:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def add_rear(self,item):
        self.items.append(item)
    
    def add_front(self,item):
        self.items.insert(0,item)
    
    def remove_rear(self):
        if self.is_empty():
            return "Underflow! Queue is empty."
        return self.items.pop()
    
    def remove_front(self):
        if self.is_empty():
            return "Underflow! Queue is empty."
        return self.items.pop(0)
    
    def peek_rear(self):
        if self.is_empty():
            return "No element to display! Queue is empty."
        return self.items[-1]
    
    def peek_front(self):
        if self.is_empty():
            return "No element to display! Queue is empty."
        return self.items[0]
    
    def size(self):
        return len(self.items)
    