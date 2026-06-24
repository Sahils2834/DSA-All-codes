#leetcode 876
#Middle of the Linked List
#Definition for singly-linked list. 
#time = O(n)
#space = O(1)

# tortoise and hare method (slow and fast pointers)

# Initialize two pointers, slow and fast, both starting at the head of the list.

# Iterate through the list while the fast pointer and its next node are not None.

# In each iteration, move the slow pointer one step forward (slow = slow.next).

# Move the fast pointer two steps forward (fast = fast.next.next).

# When the loop terminates, the slow pointer will be at the middle node of the list.

# Return the slow pointer.

class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow