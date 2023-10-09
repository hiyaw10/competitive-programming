class Solution(object):
    def findRadius(self, houses, heaters):
        
        houses.sort()
        heaters.sort()

        result = 0

        
        for house in houses:
            left = bisect.bisect_right(heaters, house) - 1
            right = bisect.bisect_left(heaters, house)

            if left < 0:
                result = max(result, heaters[0] - house)
            
            elif right >= len(heaters):
                result = max(result, house - heaters[-1])
            
            else:
                result = max(result, min(house - heaters[left], heaters[right] - house))

        
        return result
