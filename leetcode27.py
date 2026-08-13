#leetcode 27 (remove element)
#algorithm
    #use two pointer approach
#time- O(n)
#space- O(1)

class solution:
    def removeElement(self,nums,val):

        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow