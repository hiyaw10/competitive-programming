class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #let us first create a hashmap and track the index of the last occurence of a unique element.
        hashmap = {}
        output = []
        for i in range(len(s)):
            hashmap[s[i]] = i
        
        size, end = 0, 0
        for i in range(len(s)):
            end = max(end, hashmap[s[i]])
            size += 1
            if i == end:
                output.append(size)
                size = 0
        return output
