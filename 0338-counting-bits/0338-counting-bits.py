class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0] * (n+1)
        
        for num in range(1, n+1):
            temp = answer[num//2] + (num&1)
            answer[num] = temp
        return answer