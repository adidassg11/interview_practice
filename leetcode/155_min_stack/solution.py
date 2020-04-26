class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # List
        self.list_ = []
        # MinHeap?   # TODO

    def push(self, x: int) -> None:
        self.list_.append(x)

    def pop(self) -> None:
        self.list_.pop()

    def top(self) -> int:
        return self.list_[len(self.list_)-1]

    def getMin(self) -> int:
        pass
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
print(obj.top())
obj.pop()
print(obj.top())
# param_4 = obj.getMin()

