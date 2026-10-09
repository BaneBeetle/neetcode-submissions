class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # The problem as of now is we need smarter logic to detect collisions
        # The only case is -> <-
        # which will be:  + -


        # Asteroids are in a row
        # Indeces = Position
        # Abs(Value) = Size
        # + = right, - = left. Means contradicting signs will collide

        # Smaller explodes
        # Tie = both

        ptr = 0
        stack = []

        while ptr < len(asteroids):

            if not stack:
                stack.append(asteroids[ptr])

            # Check for conflicting signs
            elif (stack[-1] > 0 and asteroids[ptr] < 0):
                # I believe ther only possible scenario where there is a collision
                # is stack element = +, outsider = -
                
                add_outsider = True

                while len(stack) > 0 and stack[-1] > 0:
                    # Here outsider loses, keep popping, or both blow up
                    if abs(stack[-1]) == abs(asteroids[ptr]):
                        add_outsider = False
                        stack.pop()
                        break
                    elif abs(stack[-1]) < abs(asteroids[ptr]):
                        # outsider wins
                        stack.pop()
                    elif abs(stack[-1]) > abs(asteroids[ptr]):
                        add_outsider = False
                        break
                    

                if add_outsider:
                    stack.append(asteroids[ptr])
                # We need to exit loop IF stack is empty, first element is a negative
                # OR if both blew up.
            else:
                stack.append(asteroids[ptr])
            ptr += 1
        
        return stack
        