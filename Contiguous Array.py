class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        curr=0
        d={}
        maxi=0
        for i in range(len(nums)):
            curr+=nums[i]
            if curr==0:
                maxi=i+1
            if curr in d.keys():
                maxi=max(maxi,i-d[curr])
            else:
                d[curr]=i
        return maxi
