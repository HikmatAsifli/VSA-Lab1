import math

x = 0.5
E = 0.001
P = 0.0
term = x
n = 1

while abs(term) > E:
    P += term
    n += 1
    term = ((-1) ** n) * (x ** (2 * n - 1)) / math.factorial(2 * n - 1)


print(f"P'nin yax? n d?y?ri: {P}")