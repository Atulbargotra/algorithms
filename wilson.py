import math
from datetime import datetime
#for primility testing
n = int(input())
t1 = datetime.now()
if (math.factorial(n-1)%n == (n-1)):
    print("prime")
else:
    print("non-prime")
t2 = datetime.now()
print(t2-t1)
from math import sqrt
def prime(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True
t3 = datetime.now()
prime(n)
t4 = datetime.now()
print(t4-t3)