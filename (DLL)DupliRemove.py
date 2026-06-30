#Remove Duplicates from sorted DLL (OPTIMAL)
#Time complexity O(n)
#space complexity O(1)

def remove_duplicates(head):
    curr = head
    prev = None
    if curr.prev == head:
        curr.prev = None
        head = curr

    while curr is not None and curr.next is not None:
        if curr.val == curr.next.val:
            curr.prev.prev.next = curr
            curr.prev = curr.prev.prev
        else:
            curr = curr.next
    return head