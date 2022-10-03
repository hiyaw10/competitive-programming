class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency=[[] for i in range(len(nums)+1)]
        count={}
        for i in nums:
            count[i]=1+count.get(i,0)
        for key,value in count.items():
            frequency[value].append(key)
        result=[]
        for i in range(len(frequency)-1,0,-1):
            for number in frequency[i]:
                result.append(number)
                if len(result)==k:
                    return result
        return
        