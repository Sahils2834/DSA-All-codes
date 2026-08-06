#GFG fractional knapsack

class solution:
    def solution(self,nums,w):
        nums.sort(key = lambda x: x.value/x.weight , reverse=True)
        currW = 0
        ans = 0
        for i in nums:
            if currW + i.weight <= w:
                currW += i.weight
                ans += i.value
            else:
                ans += i.value * w / i.weight
                break
        return ans