class MinStack:

    def __init__(self):
        # create two empty stacks
        # 1. one to hold the values 
        # 2. other to hold the current minimum
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # for first stack take the input value and push it to the stack
        self.stack.append(val)
        # find the minimum value 
        # find the the value to push to minStack
        # if the minStack is not empty
        if self.minStack:
            # then return the min of current value and top value of min stack
            val = min(val, self.minStack[-1])
        self.minStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # returns the top valuer of the stack , only when its non empty
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()