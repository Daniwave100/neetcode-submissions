class Solution:
    def isValid(self, s: str) -> bool:
        # stack
        # for loop 
        stack = []
        # open_paren = {'}': "{", "]": "[", ")": "("}
        open_paren = {'{': "}", "[": "]", "(": ")"}
        

        for i in range(len(s)):
            if s[i] in open_paren.keys():
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if s[i] == open_paren[stack[-1]]:
                    stack.pop()
                else:
                    return False
                    
        if len(stack) == 0:
            return True
        else:
            return False