class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack)==0 or val <= self.getMin() :
            self.min_stack.append(val)
    def pop(self) -> None:
        if len(self.stack) == 0 or self.stack.pop() == self.getMin() :
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()