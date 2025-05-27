    #
    # Solved by Miguecetin
    # Date: 28/05/25
    #
    # https://projecteuler.net/problem=26
    # https://github.com/Miguecetin/Project-Euler-Solutions
    #
    
from math import sqrt
    
    # The period of the repeating decimal of 1/n is related to the properties of the number n. 
    # Specifically, it's related to the smallest integer k such that 10^k - 1 is divisible by n.
    
    # if get_prime_factors(i) != set([2]) and get_prime_factors(i) != set([5]): # There is no recurring cycle in this case
    
def reciprocal_cycles(rangemax: int = 1000) -> int:
    
    fractions_length = dict() # fraction: length
    
    for fraction in range(2, rangemax):
        fractions_length[fraction] = get_cycle_length(fraction)

    return max(fractions_length.keys(), key=fractions_length.get) # max fraction (key) depending on the value
    
def get_cycle_length(fraction: int) -> int:
    
    # Returns the length of the cycle for the given fraction 
    
    length = 0
    
    if get_prime_factors(fraction) != set([2]) and get_prime_factors(fraction) != set([5]): # There is no recurring cycle in this case
        pass
    else: # Cases with recurring cycles
        
        aux = True
        while (aux):
            length += 1
            if 10**length % fraction == 0:
                aux = False
    
    return length
    
def get_prime_factors(num: int) -> list:
    
    prime_factors = set()
    i = 2
    
    while (i ** 2 <= num):
        if num % i == 0:
            prime_factors.add(i)
            num //= i
        else:
            i += 1
            
    if num > 1:
        prime_factors.add(num)
    
    return prime_factors
    
if __name__ == "__main__":
    
    print(reciprocal_cycles())