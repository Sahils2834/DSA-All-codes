#leetcode 26 (remove duplicates from sorted array)
#algorithm:
    #Use two pointer approach
#time- O(n)
#space- O(1)

class solution:
    def removeDuplicates(self, nums):
        slow = 0

        for fast in range(1,len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1 
