class MinStack:

    def __init__(self):
        self.min_arr = []
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.min_arr) == 0:
            self.min_arr.append(val)
            self.stack.append(val)
        else:
            if self.min_arr[-1] < val:
                self.min_arr.append(self.min_arr[-1])
            else:
                self.min_arr.append(val)
            self.stack.append(val)
        
    def pop(self) -> None:
        self.min_arr.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]
