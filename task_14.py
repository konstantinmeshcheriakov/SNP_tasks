class EvenNumbers():
    def __init__(self, n):
        self.n = n
        self.counter = 0
    @property
    def n(self):
        return self._n
    
    @n.setter
    def n(self, value):
        if not isinstance(value, int) and value < 0:
            print('n должно быть целым и положительным числом')
        self._n = value
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.n:
            result = self.counter * 2
            self.counter += 1
            return result
        else:
            raise StopIteration
        