def multiples_of_3_or_5(number: int) -> int:
    
    # https://projecteuler.net/problem=1
    # Solved by Miguecetin
    
    return sum(num for num in range(number) if num % 3 == 0 or num % 5 == 0)

if __name__ == "__main__":
    print(multiples_of_3_or_5(1000))
