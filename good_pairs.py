class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        p=list(set(nums))
        d={}
        s=0
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for i in p:
            if d[i]>1:
                s+=d[i]*(d[i]-1)//2
        return s
