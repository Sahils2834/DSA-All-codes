# delete key from DLL (OPTIMAL)
# time complexity O(n)
# space complexity O(1)

def delete_key(head, key):
    temp = head
    prev = None
    new_head = head

    while temp is not None:

        if temp.val == key:

            if prev is not None:
                prev.next = temp.next

            if temp.next is not None:
                temp.next.prev = prev

            if temp == new_head:
                new_head = temp.next

        prev = temp
        temp = temp.next

    return new_head
