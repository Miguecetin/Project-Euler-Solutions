import math

def smallest_multiple(rangemax: int = 20) -> int:
    
    # https://projecteuler.net/problem=5
    # Solved by Miguecetin
    # Date: 04/04/25
    
    # Find the lcm (least common multiple) for numbers [1, n=20] with math.lcm()
    
    
    numbers = [i for i in range(2, rangemax + 1)]
        
    return math.lcm(*numbers)
    
if __name__ == "__main__":
    print(smallest_multiple())