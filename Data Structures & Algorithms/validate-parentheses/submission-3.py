class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        stack = [] # will keep track of our openers

        openers = set()
        openers.add("[")
        openers.add("(")
        openers.add("{")
        

        family = {"]":"[", ")": "(", "}": "{"}

        for c in s:
            if c in openers:
                stack.append(c)
            else:
                # if its not an opener then it must be a closer
                # this means that c is for sure a closer
                if len(stack) == 0:
                    return False
                else:
                    popped = stack.pop()
                    # ] [
                    if family[c] !=  popped:
                        return False

        if len(stack) > 0:
            return False

        return True

