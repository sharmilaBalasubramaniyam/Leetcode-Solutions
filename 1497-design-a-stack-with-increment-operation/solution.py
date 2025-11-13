class CustomStack:

    def __init__(self, maxSize: int):
        self.li=[]
        self.maxSize=maxSize

    def push(self, x: int) -> None:
        if len(self.li)<self.maxSize:
            self.li.append(x)
    

    def pop(self) -> int:
        if not self.li:
            return -1
        return self.li.pop()
        

    def increment(self, k: int, val: int) -> None:
        self.li[:k]=[i+val for i in self.li[:k]]
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
