class NumMatrix:

	def __init__(self, matrix: List[List[int]]):
		self.mat=matrix[:]
		for i in range(len(matrix)):
			for j in range(1,len(matrix[0])):
				self.mat[i][j]+=self.mat[i][j-1]





	def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
		s=0
		if col1==0:

			for i in range(row1,row2+1):
					s+=self.mat[i][col2]
		else:
			for i in range(row1,row2+1):
					s+=(self.mat[i][col2]-self.mat[i][col1-1])
		return s