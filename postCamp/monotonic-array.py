class Solution(object):
    def isMonotonic(self, nums):
        inc = True
        dec = True
        for i in range(len(nums) - 1):
            
            if nums[i] > nums[i + 1]:
                inc =False

            if nums[i] < nums[i+1]:
                dec = False
            

            if not inc and not dec:
                return False
        
        return True