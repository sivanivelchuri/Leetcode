class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                c+=nums[i]
            else:
                continue
        return c
        
