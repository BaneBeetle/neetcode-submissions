class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

        

    def push(self, val: int) -> None:
        # Assume push is just appending?
        self.stack.append(val)

        if self.min_stack == []:
            self.min_stack.append(val) # [1]
        else:
            print(self.min_stack)
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)



        

    def pop(self) -> None:
        # Never empty, removes whats at the top of the stack

        val = self.stack.pop()
        if val == self.min_stack[-1]:
            print("Hit")
            print(self.min_stack)

            x = self.min_stack.pop()
            print(self.min_stack)
        return
        

    def top(self) -> int:
        # Never empty
        return self.stack[-1]
        

    def getMin(self) -> int:
        # Never empty

        return self.min_stack[-1]


        
