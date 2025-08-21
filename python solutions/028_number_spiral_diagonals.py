    #
    # Solved by Miguecetin
    # Date: 22/08/25
    #
    # https://projecteuler.net/problem=28
    # https://github.com/Miguecetin/Project-Euler-Solutions
    #

    # Sum of all terms on the two principal diagonals of a 2n+1 X 2n+1 square spiral is given
    # by the formula a(n) = 1 + 10*n^2 + (16*n^3 + 26*n)/3

def number_spiral_diagonals(dimensions: int = 1001) -> int:
    
    # We solve for n in 2n+1 = 1001 -> n=500
    
    n = int( (dimensions - 1) / 2 )
    
    # And apply the formula a(n) = 1 + 10*n^2 + (16*n^3 + 26*n)/3
    
    diagonals_sum = int( 1 + 10*(n**2) + (16*(n**3) + 26*n)/3 )
    
    return diagonals_sum
    
if __name__ == "__main__":
    
    print(number_spiral_diagonals())