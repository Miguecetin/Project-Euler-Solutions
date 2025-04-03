def even_fibonacci_numbers() -> int:
    
    # https://projecteuler.net/problem=2
    # Solved by Miguecetin

    counter, na, nb = 0, 0, 1 # na = current fibonacci number. nb = next fibonacci number in the sequendce
    
    while na < 4000000:
        fib_n = na + nb
        na, nb = nb, fib_n
        
        if fib_n % 2 == 0:
            counter += fib_n
        
    return counter

if __name__ == "__main__":
    print(even_fibonacci_numbers())
