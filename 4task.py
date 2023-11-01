# Генератор списків
list_2 = [i*i for i in range(1, 10)]
print(list_2)


# Генератор
def generator_2(n):
    for i in range(1, n):
        yield i*i


generator_2 = generator_2(16)
while True:
    try:
        print(next(generator_2))
    except StopIteration:
        break
