class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations_length = len(citations)
        papers = [0]*(citations_length+1)

        for citation in citations:
            index = min(citations_length, citation)
            papers[index] += 1

        k, s = citations_length, papers[citations_length]
        while k > s:
            k -= 1
            s += papers[k]

        return k