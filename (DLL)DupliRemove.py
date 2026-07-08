#Remove Duplicates from sorted DLL (OPTIMAL)
#Time complexity O(n)
#space complexity O(1)


class Solution:
    def removeDuplicates(self, head):
        cur = head
        
        while cur:
            if cur.prev and cur.prev.data == cur.data:
                if cur.prev == head:
                    cur.prev = None        # Remove backward link
                    head = cur            # Update head to current node
                else:
                    # Remove the previous duplicate node by updating links
                    cur.prev.prev.next = cur     # Connect prev's prev to current
                    cur.prev = cur.prev.prev     # Connect current to prev's prev
            
            cur = cur.next  # Move to next node
        
        return head