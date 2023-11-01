def num_generator(n):
    for i in range(1, n):
        yield i


num_gen = num_generator(17)
while True:
    try:
        print(next(num_gen))
    except StopIteration:
        break