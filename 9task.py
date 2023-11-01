class IterList:
    def __init__(self, list_par):
        self.start = 0
        self.list = list_par
        self.end = len(list_par)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        self.start += 1
        word = self.list[self.start-1]
        if word == word[::-1]:
            return word


word_list = ["radar", "cake", "mom", "apple", "wow"]
it_list = IterList(word_list)
for i in it_list:
    if i != None:
        print(i)






