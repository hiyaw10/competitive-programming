class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n==0:
            return 0
        l, r = 0, n
        while r>l:
            mid=(l+r)//2
            if n-mid==citations[mid]:
                return n-mid
            if n-mid>citations[mid]:
                l=mid+1
            else:
                r=mid
        return (n-l) 