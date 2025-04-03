def largest_palindrome_product() -> int:
    
    # https://projecteuler.net/problem=4
    # Solved by Miguecetin
    
    largest = 0
    
    for i in range(1, 1000):
        for j in range(1, 1000):
            num = i * j
            if is_palindrome(num): # no need to add "and num > largest" since it will always be true (i and j never decrease)
                largest = num
    
    return largest

def is_palindrome(num: int) -> bool:
    
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    print(largest_palindrome_product())
