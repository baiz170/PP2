def square_generator(N):
    for i in range(N + 1):
        yield i ** 2


def even_numbers(n):
    return (str(i) for i in range(0, n + 1, 2))


def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


def countdown(n):
    for i in range(n, -1, -1):
        yield i


N = 10
print("Squares up to", N, ":", list(square_generator(N)))


n = int(input("Enter a number for even generator: "))
print("Even numbers:", ", ".join(even_numbers(n)))


n = 50
print("Numbers divisible by 3 and 4 up to", n, ":", list(divisible_by_3_and_4(n)))


a, b = 3, 7
print(f"Squares from {a} to {b}:")
for val in squares(a, b):
    print(val, end=" ")
print()


n = 5
print(f"Countdown from {n}:")
for val in countdown(n):
    print(val, end=" ")
print()
