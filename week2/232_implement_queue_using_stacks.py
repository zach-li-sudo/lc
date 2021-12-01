class MyQueue:
    def __init__(self):
        self.stack = []
        self.temp = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        while self.stack:
            elem = self.stack.pop()
            self.temp.append(elem)
        elem_to_pop = self.temp.pop()

        while self.temp:
            elem = self.temp.pop()
            self.stack.append(elem)
        return elem_to_pop

    def peek(self) -> int:
        while self.stack:
            elem = self.stack.pop()
            self.temp.append(elem)
        elem_to_peek = self.temp[-1]
        while self.temp:
            elem = self.temp.pop()
            self.stack.append(elem)
        return elem_to_peek

    def empty(self) -> bool:
        return False if self.stack else True
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)

param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()


print(param_2, param_3, param_4)