#### 1, 1, 2, 3, 5, 8, 13, .... fib(n) = fib(n-1) + fob(n-2)


def fibo(n, cache={}):
    if n == 0 or n ==1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = fibo(n-1) + fibo(n-2)
        return cache[n]

def fibo_behtart(n):
    if n == 0 or n ==1:
        return 1
    else:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a+b
    return a

print(fibo(150))
# print(fibo_behtart(1500))