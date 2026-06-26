#length of loop in a LL
#1->2->3->4->5
#     ^
#     |
#     6
#slow:1->2->3->4->5->6->3
#fast:1->3->5->4->6->2->4
#meet at 4
#len of loop: 4
#slow:4->5->6->3->4
#len of loop: 4

class Solution(object):
    def lengthOfLoop(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow == fast:
            count = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                count += 1
            return count
        return 0