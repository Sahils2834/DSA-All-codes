#Minimum number of coins
#greedy approach
class solution:
    def solution(self,coins,amount):
        coins.sort(reverse=True)
        result = []
        n = len(coins)
        for i in range(n-1, -1 ,-1):
            while amount >= coins[i]:
                amount -= coins[i]
                result.append(coins[i])
        return result    
    
    