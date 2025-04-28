    #
    # Solved by Miguecetin
    # Date: 28/04/25
    #
    # https://projecteuler.net/problem=21
    # https://github.com/Miguecetin/Project-Euler-Solutions
    #
# TODO test on projecteuler
def amicable_numbers(rangemax: int = 10000) -> int:
    # TODO remove this explanation
    # Let d(n) be defined as the sum of proper divisors of n
    # if d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each a and b are called amicable numbers
    # Example: d(220) = 1,2,4,5,10,11,20,22,44,55,110 = 284.
    # Then d(284) = 1,2,4,71,142 = 220
    # Then, 284 and 220 are amicable numbers
    # Return the sum of all amicable numbers under 10000
    
    amicables = [] # List of all amicable numbers under 10000
    for a in range(1, rangemax + 1):
        divisors_a = get_proper_divisors(a)
        b = d(divisors_a)
        
        divisors_b = get_proper_divisors(b)
        c = d(divisors_b)
        
        if b == c and b != a:
            amicables.append(a)
            amicables.append(b)

    return sum(i for i in set(amicables))

def get_proper_divisors(number: int) -> list:
    
    return [i for i in range(1, int(number / 2 + 1)) if i % number == 0]

def d(divisors: list) -> int:
    return sum(i for i in divisors)

if __name__ == "__main__":
    
    print(amicable_numbers())
