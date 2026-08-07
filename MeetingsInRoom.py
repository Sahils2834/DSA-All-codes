#Meeting in rooms
#algorithm : We will use a greedy approach. We will sort the meetings by their end times. Then, we will iterate through the sorted meetings and add the meetings to the result if they do not overlap with the previous meeting.    
#time complexity : O(n log n) because we are sorting the meetings
#space complexity : O(n) because we are storing the meetings


class meeting:
    def __init__(self,start,end,posi):
        n =len(start)
        self.start = start
        self.end = end
        self.posi = posi
        meet = [meet(start[i], end[i], i+1) for i in range(n)]
        meet.sort(key = lambda x: x.end)
        result = [1]
        count = 1
        last = meet[0].end
        for i in range(1, n):
            if meet[i].start > last:
                result.append(meet[i].posi)
                count += 1
                last = meet[i].end
        return result, count

        