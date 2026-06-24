#Insert in Linked list in between anywhere
#time = O(n)
#space = O(1)

class Solution:
    def insert(self, head, val, pos):
        new_node = Node(val)

        if pos == 0:
            new_node.next = head
            return new_node
        
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < pos:
                prev_node = current
                current = current.next
                count += 1

            prev_node.next = new_node
            new_node.next = current

            return head 
