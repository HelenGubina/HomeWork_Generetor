class MyIter:
    def __init__(self, str_par):
        self.start = 0
        self.end = len(str_par)
        self.str = str_par

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        self.start += 1
        return self.str[self.start-1]


my_iter = MyIter("Helen")
for i in my_iter:
    print(i)
