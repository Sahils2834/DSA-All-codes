#DLL Append
#case 1: empty list
#case 2: single node list
#case 3: multiple node list


class DLL:
    def __init__(self,data):
        self.head=None

    def insert(self,val):
        new_node = Node(val)
        if  not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node