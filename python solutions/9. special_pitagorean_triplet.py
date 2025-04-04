    #
    # Solved by Miguecetin
    # Date: 05/04/25
    #
    # https://projecteuler.net/problem=9
    # https://github.com/Miguecetin/Project-Euler-Solutions
    #

def pitagorean_triplet(sum: int = 1000) -> int:
    
    # Implementation without clever math, just brute force.
    
    for a in range(1, sum + 1):
        for b in range(1, sum + 1):
            for c in range(1, sum + 1):
                if (a ** 2 + b ** 2 == c ** 2) and (a + b + c == sum):
                    # Solution also works if we do `a, b = b, a` (the order of a and b don't matter)
                    return a * b * c
            

if __name__ == "__main__":
    print(pitagorean_triplet())