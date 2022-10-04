class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [None]*len(temperatures)
        waiting_list = []
        for day, temp in enumerate(temperatures):
            # clearing up the previous waiting days
            if len(waiting_list) > 0:
                while len(waiting_list) > 0:
                    d, t = waiting_list[-1]
                    if temp > t:
                        ans[d] = day-d
                        waiting_list.pop(-1)
                    else:
                        break
            waiting_list.append((day, temp))
        
        ans = [0 if a is None else a for a in ans]
        
        return ans
                