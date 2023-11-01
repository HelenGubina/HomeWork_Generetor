def even_generator(n):
    for i in range(1, n):
        if i % 2 = 0:
            yield i


even = even_generator(17)
while True:
    try:
        print(next(even))
    except StopIteration:
        break