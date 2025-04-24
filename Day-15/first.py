class MyNumbers:

    def __init__(self,maximum,minimum):
        self.maximum = maximum
        self.minimum = minimum

    def __str__(self):
        return f"MyNumbers {self.minimum} {self.maximum}"

    def __repr__(self):
        pass

    def _iter_(self):
        self.a = self.minimum
        return self
    
    def __repr__(self):
        pass

    def __next__(self):
        if self.a <= self.maximum:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

m = MyNumbers(1, 10)
print(m)