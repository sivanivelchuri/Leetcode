class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d={}
        s=0
        for i in stones:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for i in range(len(jewels)):
            if jewels[i] in d:
                s+=d[jewels[i]]
        return s
        
