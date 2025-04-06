    #
    # Solved by Miguecetin
    # Date: 06/04/25
    #
    # https://projecteuler.net/problem=14
    # https://github.com/Miguecetin/Project-Euler-Solutions
    #

from collections import defaultdict

def longest_collatz_sequence(rangemax: int = 1000000) -> dict:
    
    sequences = defaultdict(list)
    
    for starter in range(1, rangemax):
        
        i = starter
        sequences[starter].append(starter)

        while (i > 1):
            
            if (i % 2 == 0): # Case for even numbers
                i = i // 2
            else:
                i = i * 3 + 1
            
            sequences[starter].append(i)
        
    return sequences
        
if __name__ == "__main__":
    
    longest_sequence = longest_collatz_sequence(1000000)
    
    longest = 1
    for i, j in longest_sequence.items():
        # print(i, j)
        if len(j) >= longest:
            longest = i

    print(f"Longest: {longest} // Total length: {len(longest_sequence[longest])} // Sequence: {longest_sequence[longest]}")