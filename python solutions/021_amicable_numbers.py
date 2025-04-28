    #
    # Solved by Miguecetin
    # Date:28/04/25
    #
    # https://projecteuler.net/problem=21
    # https://github.com/Miguecetin/Project-Euler-Solutions
    #
    
def amicable_numbers(rangemax: int = 10000) -> int:
    # Let d(n) be defined as the sum of proper divisors of n
    # if d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each a and b are called amicable numbers
    # Example: d(220) = 1,2,4,5,10,11,20,22,44,55,110 = 284.
    # Then d(284) = 1,2,4,71,142 = 220
    # Then, 284 and 220 are amicable numbers
    # Return the sum of all amicable numbers under 10000
    
    amicables = [] # List of all amicable numbers under 10000
    for n in range(1, rangemax + 1):
        divisors = get_proper_divisors(n) 
        b = sum(i for i in divisors)
        # b = d(n), now we need to get c = d(d(n)) and see if n == c, in which case they are amicable
        
        if n != b:
            divisors = get_proper_divisors(b)
            c = sum(i for i in divisors)
            
            if c == n: # if this is true, then n and b are amicable
                amicables.append(n, b)

    return sum(i for i in amicables)

def get_proper_divisors(number: int) -> list:
    
    return [i for i in range(1, int(number / 2 + 1)) if i % number == 0]

if __name__ == "__main__":
    
    print(amicable_numbers())
