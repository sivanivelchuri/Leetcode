class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x=sorted(nums)
        y=[]
        c=0
        for i in range(len(nums)):
            j=x.index(nums[i])
            y.append(j)
        return (y)
