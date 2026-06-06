from typing import List
from math import sqrt


def factors(num: int) -> List[int]:
    factors = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if num // i != i:
                factors.append(num // i)
    factors.sort()  
    return factors