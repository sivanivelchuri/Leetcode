class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk=[-1]
        string=s
        n=len(string)
        result = 0
        for i in range(n):
            if string[i] == '(':
                stk.append(i)
            else:  
                if len(stk) != 0:
                    stk.pop()
            if len(stk) != 0:
                result = max(result,i - stk[len(stk)-1])
            else:
                stk.append(i)
        return result
 
 
            
        
