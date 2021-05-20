class Solution:
    def countPrimes(self, n: int) -> int:
        seive=[1]*(n)
        i=2
        while(i*i<=n+1):
            if seive[i]==1:
                j=i*i
                while j<n:
                    seive[j]=0
                    j+=i
            i+=1
        c=0
        k=2
        while k<n:
            if seive[k]==1:
                c+=1
            k+=1
        return c
