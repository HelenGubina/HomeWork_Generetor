def fibonacci(n, f1=0, f2=1):
    for i in range(n):
        if i == 0 or i == 1:
            yield i
        else:
            f1, f2 = f2, f1 + f2
            yield f2


fib = fibonacci(6)
while True:
    try:
        print(next(fib))
    except StopIteration:
        break
