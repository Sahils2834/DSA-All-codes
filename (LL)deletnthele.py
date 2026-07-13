#delete n'th node from end
# leetcode 19 delete nth node from end of linked list
# 1->2->3->4->5->NULL
# n=2
# result: 1->2->3->5->NULL


class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head