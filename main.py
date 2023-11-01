def even_odd_generator(n):
    for i in range(1, n):
        if i % 15 == 0:
            yield "FizzBuzz"
        elif i % 5 == 0:
            yield "Buzz"
        elif i % 3 == 0:
            yield "Fizz"

even_odd = even_odd_generator(16)
while True:
    try:
        print(next(even_odd))
    except StopIteration:
        break

