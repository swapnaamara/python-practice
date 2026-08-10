class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        val = self.start
        self.start -= 1
        return val

for i in Countdown(5):
    print(i) # 5 4 3 2 1