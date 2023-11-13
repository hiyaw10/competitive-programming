class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hashmap = {}
        max_freq = 1
        min_len = 1
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = (i, 1)
            else:
                entry = hashmap[nums[i]]
                cur_freq = entry[1] + 1
                if cur_freq > max_freq:
                    max_freq = cur_freq
                    min_len = i - entry[0] + 1
                    
                elif cur_freq == max_freq:
                    if (i - entry[0] + 1 < min_len):
                        min_len = i - entry[0] + 1
                
                hashmap[nums[i]] = (entry[0], cur_freq)
        return min_len
            