class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        X = (num - 3)/3
        if X == int(X):
            X = int(X)
            return [X, X+1, X+2]
        return []