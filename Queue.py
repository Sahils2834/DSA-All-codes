#Queue implementation using list
#FIFO
#time complecity O(1)
#space complecity O(n)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            return "Underflow! Queue is empty."
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "No element to display! Queue is empty."
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Driver code
queue = Queue()

print(f"Is queue empty? {queue.is_empty()}")

queue.enqueue(50)
queue.enqueue(70)
queue.enqueue(25)

print(f"Queue elements: {queue.items}")
print(f"Dequeue: {queue.dequeue()}")
print(f"Peek: {queue.peek()}")
print(f"Size of queue: {queue.size()}")
print(f"Is queue empty? {queue.is_empty()}")