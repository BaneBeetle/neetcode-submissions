class Solution:
    def isValid(self, s: str) -> bool:

        ptr = 0

        stack = []

        while ptr < len(s):
            
            if s[ptr] in '([{':
                stack.append(s[ptr])
            else:
                if not stack:
                    return False
                elif s[ptr] == ')':
                    popped = stack.pop()
                    if popped != '(':
                        return False
                elif s[ptr] == ']':
                    popped = stack.pop()
                    if popped != '[':
                        return False
                elif s[ptr] == '}':
                    popped = stack.pop()
                    if popped != '{':
                        return False
                
            ptr += 1
        if stack:
            return False
        return True
        