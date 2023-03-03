class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for first, last, seat in bookings:
            
            if first <= n: ans[first-1] += seat
            if last < n: ans[last] -= seat
        Sum = 0
        for i in range(len(ans)):
            Sum += ans[i]
            ans[i] = Sum
        return ans