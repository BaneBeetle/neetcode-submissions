class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        ptr = 0
        ret = ""

        invalid_indeces = [] # will include all invalid indices 
        paranthesis_stack = []

        while ptr < len(s):

            if s[ptr] == '(':
                paranthesis_stack.append('(')
                invalid_indeces.append(ptr)

            elif s[ptr] == ')':
                if not paranthesis_stack:
                    paranthesis_stack.append(')')
                    invalid_indeces.append(ptr)

                elif paranthesis_stack[-1] == '(':
                    # pop logic
                    invalid_indeces.pop()
                    paranthesis_stack.pop()
                else:
                    paranthesis_stack.append(')')
                    invalid_indeces.append(ptr)

            ptr += 1
        
        # Now invalid_Stack should contain all indexes we want to skip
        
        ptr1 = 0
        while ptr1 < len(s):
            if ptr1 not in invalid_indeces:
                ret += s[ptr1]
            
            ptr1 += 1

    
        return ret