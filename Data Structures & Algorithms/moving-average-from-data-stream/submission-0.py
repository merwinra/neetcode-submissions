class MovingAverage:

    def __init__(self, size: int):
        self.__size = size
        self.__q = deque()
        self.__sum = 0
        

    def next(self, val: int) -> float:
        if len(self.__q) == self.__size:
            v = self.__q.popleft()
            self.__sum -= v
        
        self.__q.append(val)
        self.__sum += val
        return self.__sum / len(self.__q)        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
