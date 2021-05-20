class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        d={0:1}
        c=0
        curr_sum=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if curr_sum-k in d:
                c+=d[curr_sum-k]
            if curr_sum not in d:
                d[curr_sum]=1
            else:
                d[curr_sum]+=1
        return c
