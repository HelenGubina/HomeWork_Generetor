def num_generator(n):
    for i in range(1, n):
        prime = True
        for j in range(1, i):
            if i % j == 0 and i != j and j != 1:
                prime = False
                break
        if prime:
            yield i


num_gen = num_generator(18)
while True:
    try:
        print(next(num_gen))
    except StopIteration:
        break