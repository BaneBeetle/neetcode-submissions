class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # initialize 2 stacks, num stack and operator stack
        # whenever we see an operator, we dump everything from the num stack.

        # now that I explain it, idk if I even need an operator_stack but whatever

        num_stack = []

        # .isdigit()
        # we know that elements in list can either be operator or digit

        result = None

        # currently, the assumptions I am making is if they just give [2, 3] this is invalid since we cant return two numbers.

        if len(tokens) == 1 and tokens[0].isdigit():
            # But in a case where [1], where there is just a list of 1 int, then we can just return that
            return int(tokens[0])
        
        for t in tokens:
            if t == "+":
                val2 = num_stack.pop()
                val1 = num_stack.pop()
                result = val1 + val2

                num_stack.append(result)
            elif t == "-":
                val2 = num_stack.pop()
                val1 = num_stack.pop()
                result = val1 - val2
                num_stack.append(result)
                
            elif t == "*":
                val2 = num_stack.pop()
                val1 = num_stack.pop()
                result = val1 * val2
                num_stack.append(result)
            elif t == "/":
                val2 = num_stack.pop()
                val1 = num_stack.pop()
                result = int(val1 / val2)
                num_stack.append(result)
            
            else:
                num_stack.append(int(t))
                    



        return result