class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        start = 0
        end = 0
        maxL = 0
        defdic = defaultdict()
        while end < len(s):
            if s[end] in defdic:
                start = max(defdic[s[end]]+1, start)
            maxL = max(maxL, end-start+1)
            defdic[s[end]] = end
            end+=1
        return maxL
                