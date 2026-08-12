#leetcode 21 : Merge Two Sorted Lists
#Algorithm
#1. Create a dummy node to store the merged list.
#2. Create a pointer to the dummy node.
#3. Iterate through both lists and compare the values.
#4. If the value of the first list is smaller, add it to the merged list and move the pointer of the first list forward.
#5. Otherwise, add the value of the second list to the merged list and move the pointer of the second list forward.
#6. Return the merged list.
#time complexity: O(n)
#space complexity: O(1)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next