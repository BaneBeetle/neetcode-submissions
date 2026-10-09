class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        prev_operation = ""
        current_num = ""
        
        ptr = 0

        while ptr < len(s):
            while ptr < len(s) and s[ptr] == " ":
                ptr += 1
                
            if ptr >= len(s):
                break

            if s[ptr] not in "+-/*":
                current_num += s[ptr]
            else:
                if prev_operation == "*":
                    popped = stack.pop()
                    stack.append(popped * int(current_num))
                elif prev_operation == "/":
                    popped = stack.pop()
                    stack.append(int(popped / int(current_num)))
                elif prev_operation == "-":
                    stack.append(-int(current_num))
                else:
                    stack.append(int(current_num))
                
                current_num = ""
                prev_operation = s[ptr]

            ptr += 1

        if prev_operation == "*":
            popped = stack.pop()
            stack.append(popped * int(current_num))
        elif prev_operation == "/":
            popped = stack.pop()
            stack.append(int(popped / int(current_num)))
        elif prev_operation == "-":
            stack.append(-int(current_num))
        else:
            stack.append(int(current_num))
            
        return sum(stack)