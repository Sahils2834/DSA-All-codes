#next greater element1
#algorithm = use a monotonic stack to find next greater element for nums2
#traverse nums2 from right to left; pop stack while top <= current element
#if stack is not empty, top is next greater, else -1; store in a hash map for O(1) lookup
#finally, map each element in nums1 to its next greater using the hash map
#time complexity = O(n)
#space complexity = O(n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mp ={}
        for i in range(len(nums2)- 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                mp[nums2[i]] = stack[-1]
            else:
                mp[nums2[i]] = -1
            stack.append(nums2[i])
        
        ans = []

        for num in nums1:
            ans.append(mp[num])
        return ans