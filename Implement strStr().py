class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)>=len(needle):
            for i in range(len(needle)):
                if needle in haystack:
                    return haystack.find(needle)
                elif needle not in haystack:
                    return -1
            else:
                return 0
        else:
            return -1

