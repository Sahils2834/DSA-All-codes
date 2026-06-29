#Doubly linked list
# delete

class DLL:
    def __init__(self,data):
        self.head=None

    def delete(self,val):
        new_node = Node(val)
        if  not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node