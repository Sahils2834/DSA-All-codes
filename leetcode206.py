# Reverse Linked List
#time = O(n)
#space = O(1)

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev   