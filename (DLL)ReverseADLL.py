#DLL Reverse (optimal)
#time complexity O(n)
#space complexity O(1)
# we use 3 pointers to reverse the list

def reverse(self,val,temp,head):
    if head.next is None:
        return head

    curr = head
    prev = None
    while curr is not None:
        front = curr.next
        curr.next = prev
        curr.prev = front
        prev = curr
        curr = front
    return prev