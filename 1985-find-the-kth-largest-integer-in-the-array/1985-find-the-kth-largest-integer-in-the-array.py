class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def sorter(x, y):
            n, m = len(x), len(y)
            if n < m: # if you want to keep x in left of y, return -1, here if len(x) is shorter, so it is smaller, so left # ['33', '4'], 4 to left
                return -1
            elif n > m: # +1, if to keep in right of y
                return 1
            else:
                for i in range(n):
                    if x[i] < y[i]: # if x[i] smaller, then left
                        return -1
                    elif x[i] > y[i]: # else in right 
                        return 1
                    else:
                        continue
            return 0 # if both same, x==y
            
        key = cmp_to_key(sorter)
        nums.sort(key=key, reverse=True)
        # print(nums)
        return nums[k-1]
        