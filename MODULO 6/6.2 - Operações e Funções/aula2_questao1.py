import random

va = [random.randint(-100, 100) for _ in range(20)]
lo = sorted(va)
print(va)
print(lo)
print(lo[0])
print(lo[-1])
