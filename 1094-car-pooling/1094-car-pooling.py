class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans = [0] * 1002
        
        for num, start, end in trips:
            ans[start] += num
            ans[end] -= num
        print(ans)
        runningSum = 0
        for i in range(len(ans)):
            runningSum += ans[i]
            if runningSum > capacity:
                return False
        return True