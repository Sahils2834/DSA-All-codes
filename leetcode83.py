#leetcode 83. Remove Duplicates from Sorted List
#algorithm:
#1. Use a two-pointer approach
#2. Move the `current` pointer to the next non-duplicate node
#3. Skip all nodes with the same value as `current`
#4. Connect `current` to the next non-duplicate node
#5. Time complexity: O(n)
#6. Space complexity: O(1)

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None

        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head