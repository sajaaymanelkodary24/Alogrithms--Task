import random
from timeit import timeit

def schoolbook(x, y):
    return x*y

def karatsuba(x, y):
    if x < 0 or y < 0:
        sign = -1 if (x < 0) != (y < 0) else 1
        return sign * karatsuba(abs(x), abs(y))
    if x < 10 or y < 10:
        return x*y
    digits = max(len(str(x)), len(str(y)))
    half = digits//2
    scale = 10**half
    high_x, low_x = divmod(x, scale)
    high_y, low_y = divmod(y, scale)
    z0 = karatsuba(low_x, low_y)
    z2 = karatsuba(high_x, high_y)
    z1 = karatsuba(low_x+high_x, low_y+high_y)-z0-z2
    return z2*scale*scale + z1*scale + z0

if __name__ == "__main__":
    for digits in (10, 50, 100, 300, 500):
        lower, upper = 10**(digits-1), 10**digits-1
        x, y = random.randint(lower, upper), random.randint(lower, upper)
        print(f"\nDigits: {digits}")
        for label, method in (("Schoolbook", schoolbook), ("Karatsuba", karatsuba)):
            elapsed = timeit(lambda: method(x,y), number=3)
            print(f"{label:10}: {elapsed:.6f}s")
        assert schoolbook(x,y) == karatsuba(x,y)
