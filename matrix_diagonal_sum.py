class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        pd=sd=0
        n=len(mat)
        j=n-1
        for i in range(n):
            pd+=mat[i][i]
            if i!=j:
                sd+=mat[i][j]
            j-=1
        return (pd+sd)
        
