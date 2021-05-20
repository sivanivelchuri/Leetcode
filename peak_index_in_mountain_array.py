class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i=0
        j=len(arr)-1
        while i<=j:
            m=(i+j)//2
            if arr[m]>arr[m+1] and arr[m]>arr[m-1]:
                return m
            elif arr[m]>arr[m+1] and arr[m]<arr[m-1]:
                j=m-1
            elif arr[m]>arr[m-1] and arr[m]<arr[m+1]:
                i=m+1
            
