class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        ptr = 0

        while ptr < len(s):

            if s[ptr] in "({[":
                stack.append(s[ptr])
            else:
                
                if not stack:
                    return False

                if s[ptr] == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif s[ptr] == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                elif s[ptr] == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False

            ptr += 1
        
        if len(stack) > 0:
            return False
        
        return True
        

        