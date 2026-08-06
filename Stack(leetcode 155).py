#leetcode 155-min stack
#algorithm = store a tuple or list of [value, current_min] at each level of the stack
#when pushing, current_min = min(value, min_of_element_below_it)
#this ensures O(1) retrieval of the minimum element at any given state of the stack
# Time complexity: O(1)
# Space complexity: O(n)

class MinStack:

    def __init__(self):
        self.items = []

    def push(self, value: int) -> None:
        if len(self.items) == 0:
            self.items.append([value, value])
        else:
            mini = min(self.items[-1][1], value)
            self.items.append([value, mini])

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1][0]

    def getMin(self) -> int:
        return self.items[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()