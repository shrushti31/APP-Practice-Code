# Custom Iterator Example

class Numbers:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

num = Numbers(1, 5)

for i in num:
    print(i)