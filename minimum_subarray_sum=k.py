class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        z=[]
        i=0
        curr_sum=0
        for j in range(len(nums)):
            curr_sum+=nums[j]
            while curr_sum>=s:
                z.append(j-i+1)
                curr_sum-=nums[i]
                i+=1
        if z:
            return min(z)
        else:
            return 0
