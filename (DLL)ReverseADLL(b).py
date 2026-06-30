#DLL Reverse (brute force )
#time complexity O(n)
#space complexity O(n)
#we use stack data structure to reverse the list first traverse the list and push the data into the stack 
#then traverse the list again and pop the data from the stack and push it into the list

def reverse(self,val,temp,stack):
    temp = self.head
    while temp is not None:
        stack.append(temp.data)
        temp=temp.next
    
    temp = self.head
    while temp is not None:
        e=stack.pop()
        temp.data = e
        temp = temp.next
    return self.head
        