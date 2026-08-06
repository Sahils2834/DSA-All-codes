#leetcode 455 Assign cookies
#Algo: use 2 pointer approach, sort both arrays, increment pointer of cookie if cookie is smaller than child's greed
#tc: O(nlogn)


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        n = len(g) 
        m = len(s)
        count = 0
        left = 0 
        right = 0

        while left < n and right < m:

            if s[right] >= g[left]:
                count += 1
                left += 1
                right += 1
            else:
                right += 1

        return count
        