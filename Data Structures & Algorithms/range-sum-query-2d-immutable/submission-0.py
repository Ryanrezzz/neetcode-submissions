class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.rows=len(matrix)
        self.cols=len(matrix[0])

        self.prefix= [[0]*self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                if i==0 and j==0:
                    self.prefix[i][j]=self.matrix[i][j]
                elif i==0:
                    self.prefix[i][j]=self.matrix[i][j]+self.prefix[i][j-1]
                elif j==0:
                    self.prefix[i][j]=self.matrix[i][j]+self.prefix[i-1][j]
                else:
                    self.prefix[i][j]=self.matrix[i][j]+self.prefix[i-1][j]+self.prefix[i][j-1]-self.prefix[i-1][j-1]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
      
        ans = self.prefix[row2][col2]
        if row1>0:
            ans -= self.prefix[row1-1][col2]
        if col1>0:
            ans-= self.prefix[row2][col1-1]
        if row1>0 and col1>0:
            ans+= self.prefix[row1-1][col1-1]
        return ans


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)