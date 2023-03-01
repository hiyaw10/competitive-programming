class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1001
        
        for person, start, end in trips:
            arr[start] += person
            arr[end] -= person
           
        run = 0
        for i in range(len(arr)):
            run += arr[i]
            if run > capacity:
                return False
            arr[i] = run
        return True
        