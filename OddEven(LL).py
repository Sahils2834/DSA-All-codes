#leetcode 328 Odd Even Linked List
# 1->2->3->4->5->6->NULL
#odd : 1->3->5-> NULL
#even : 2->4->6->NULL

class Solution(object):
    def oddEvenList(self, head):

        if head is None:
            return None

        odd = head
        even = head.next
        even_head = even

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head

        return head