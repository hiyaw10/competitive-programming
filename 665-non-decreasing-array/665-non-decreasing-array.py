class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed=False
        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                continue
            if changed:
                return False
            if i==0 or nums[i+1]>=nums[i-1]:
                nums[i]=nums[i+1]
            else:
                nums[i+1]=nums[i]
            changed=True
        return True
# EXPLANATION:-
    # We will iterate through the array and if the current element is smaller than the next one, we will conitnue
    # We will check if next element is greater than equal to previous element and if it is, we will swap the current element with next one
    # Else we will swap the next element with current one
    # We will return false if we have changed else return true at last
	