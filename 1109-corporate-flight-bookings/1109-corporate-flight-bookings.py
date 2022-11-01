class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * (n+1)
        #mark the range with the deltas (head and tail)
        for booking in bookings:
            #start
            result[booking[0]-1] += booking[2]
            #end
            result[booking[1]] -= booking[2]
        #cumulative sum processing
        tmp = 0
        for i in range(n):
            tmp += result[i]
            result[i] = tmp
        return result[:n]