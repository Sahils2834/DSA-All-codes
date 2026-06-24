#leetcode 876 brute force method
#time = O(n)
#space = O(n)

# Approach 1: Store nodes in an array and return the middle one
# Initialize an empty list to store the nodes.
# Traverse the linked list and append each node to the list.
# Calculate the middle index: length // 2.
# Return the node at the middle index.

class Solution(object):
    def middleNode(self, head):
        temp = head
        n = 0
        while temp is not None:
            temp = temp.next
            n += 1    
        mid = n // 2 # for single list, we can do this, but if there are two middle nodes, we will return the second middle node.
        temp = head
        for _ in range(mid):
            temp = temp.next
        return temp
