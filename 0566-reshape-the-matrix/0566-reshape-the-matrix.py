class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        final_ans = []
        flatten_array = []
        
        #we first flatten our given matrix into a 1d.
        for i in mat:
            for j in i:
                flatten_array.append(j)
        #check for legality
        if len(flatten_array) != (r * c):
            return mat
        
        for i in range(r):
            a = i * c
            b = (i * c) + c 
            final_ans.append(flatten_array[a : b])
        return final_ans