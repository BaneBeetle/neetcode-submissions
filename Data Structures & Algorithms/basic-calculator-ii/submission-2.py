class Solution:
    def calculate(self, s: str) -> int:

        # MDAS
        operations = "*/+-" # if its in this, its a operation

        stack = []
        prev_operation = None
        ptr = 0
        saved_num = ""
        while ptr < len(s):

            if s[ptr] == " ":
                ptr += 1
                continue
            
            if s[ptr] not in operations:
                # must be a number
                saved_num += s[ptr]

            # If current element is a operation
            elif prev_operation == "*":
                popped = stack.pop()
                stack.append(popped * int(saved_num))
                prev_operation = s[ptr]
                saved_num = ""
            elif prev_operation == "/":
                popped = stack.pop()
                stack.append(int(popped / int(saved_num)))
                prev_operation = s[ptr]
                saved_num = ""
            elif prev_operation == "+" or prev_operation == None:
                stack.append(int(saved_num))
                prev_operation = s[ptr]
                saved_num = ""
            elif prev_operation == "-":
                stack.append(0 - int(saved_num))
                prev_operation = s[ptr]
                saved_num = ""

            ptr += 1


        if prev_operation == "*":
            popped = stack.pop()
            stack.append(popped * int(saved_num))
        elif prev_operation == "/":
            popped = stack.pop()
            stack.append(int(popped / int(saved_num)))
        elif prev_operation == "+" or prev_operation == None:
            stack.append(int(saved_num))
        elif prev_operation == "-":
            stack.append(0 - int(saved_num))
 
            
        return sum(stack)
