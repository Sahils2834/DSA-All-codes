#linked list delete operation
#time = O(n)
#space = O(1)

#delete from end

class Solution(object):
    def deleteNode(self, head, val):

        if head is None:
            return None

        if head.val == val:
            return head.next

        temp = head
        prev = None

        while temp is not None:
            if temp.val == val:
                break

            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return head

        prev.next = temp.next

        return head