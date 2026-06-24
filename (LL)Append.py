#Append function in linked list
#time = O(n)
#space = O(1)

class Solution:
    def append(self, head, val):
        new_node = Node(val)

        if head is None:
            return new_node

        current = head

        while current.next is not None:
            current = current.next

        current.next = new_node

        return head