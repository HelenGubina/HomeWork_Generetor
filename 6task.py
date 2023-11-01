def odd_generator(n):
    for i in range(1, n):
        if i % 2 != 0:
            yield i


odd = odd_generator(16)
while True:
    try:
        print(next(odd))
    except StopIteration:
        break