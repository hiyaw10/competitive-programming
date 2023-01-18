class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        count = 0
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                count += 1
            if arr[i] < arr[i+1] and arr[i] < arr[i-1]:
                return False
            if arr[i] == arr[i+1]:
                return False
        return count == 1