class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        beg, end, ans = 0, len(people) - 1, 0
        while beg <= end:
            if people[beg] + people[end] <= limit:
                beg += 1
            ans += 1
            end -= 1
                
        return ans