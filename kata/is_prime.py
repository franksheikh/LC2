import math

def is_prime(num):
    if num <= 1:
        return False
    
    root = int(math.sqrt(num))
    
    for i in range(2, root + 1):
        if num % i == 0:
            return False
    return True

