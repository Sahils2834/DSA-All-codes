#generate binary number from 1 to n such that the corressponding index shouldn't have the value one (1's cant be at odd places)
#algorithm = use recursion with a flag; at each index place '0' and recurse
#only place '1' at index if the flag is True (meaning previous digit was '0')
#after placing '1', recurse with flag=False (next digit cannot be '1' again)
#flag ensures no two consecutive '1's appear
#when index reaches n, add the string to result
#tc -- O(2^n)
#sc --> O(n)


class solution:
    def solve(self,ind,flag,nums,result):
        if ind >=len(nums):
            result.append("".join(nums))
            return 
        nums[ind] = "0"
        self.solve(ind + 1,True, nums, result)

        if flag == True:
            nums[ind] = "1"
            self.solve(ind + 1,False,nums, result)
            nums[ind] = "0"

    def generate(self,n):
        nums = ["0"]*n
        result = []
        self.solve(0,True,nums,result)
        return result
