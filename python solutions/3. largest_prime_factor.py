    #
    # Solved by Miguecetin
    # Date: 03/04/25
    #
    # https://projecteuler.net/problem=3
    # https://github.com/Miguecetin/Project-Euler-Solutions
    #

def largest_prime_factor(number: int = 600851475143) -> int:
    
    factors = []
    
    for i in range(1, int(number**0.5 + 1)): # prime numbers must be in range [1, ceil(sqrt(number))]
        
        if number % i == 0: # if number is divisible by i => i is a prime factor
            factors.append(i) # save the prime factor
            number = number // i # reduce the search to floor(number/i), or we would get false prime factors

    return max(factors)

if __name__ == "__main__":
    print(largest_prime_factor())
