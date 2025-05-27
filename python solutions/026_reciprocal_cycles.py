    #
    # Solved by Miguecetin
    # Date: 28/05/25
    #
    # https://projecteuler.net/problem=26
    # https://github.com/Miguecetin/Project-Euler-Solutions
    #
    
def reciprocal_cycles(rangemax: int = 1000) -> int:
    
    # a = b * q + r //// r = a - (b * q)
    
    fractions_length = dict() # fraction: length
    
    for fraction in range(1, rangemax):
        cycle_length = len(str(get_cycle(fraction)))
        fractions_length[fraction] = cycle_length

    return max(fractions_length.keys(), key=fractions_length.items()) # max fracción (key) depending on the value
    
def get_cycle(fraction: int) -> int:
    
    # a = dividendo = 1
    # b = divisor = fraction
    # q = cociente 
    
    # q = (a - r) / b
    
if __name__ == "__main__":
    
    print(reciprocal_cycles())
