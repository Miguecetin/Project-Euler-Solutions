    #
    # Solved by Miguecetin
    # Date: 06/04/25
    #
    # https://projecteuler.net/problem=18
    # https://github.com/Miguecetin/Project-Euler-Solutions
    #
    
def maximum_path_sum(triangle: list) -> int:
      
    current_index = 0
    product_counter = 1
      
    for i in range(len(triangle)):
        
        tuple = triangle[i]
        
        product_counter *= tuple[current_index]
        
        if current_index == 0:
            possible_indexes = (0, 1)
        else:
            possible_indexes = (current_index, current_index + 1)
        
        if triangle.index(tuple) < len(triangle) - 1:
            current_index = select_next_index(triangle[triangle.index(tuple) + 1], possible_indexes)
        
    return product_counter
        
def select_next_index(next_tuple: tuple, possible_indexes: tuple) -> int:
    
    biggest_possible = max((next_tuple[possible_indexes[0]], next_tuple[possible_indexes[1]]))
    
    return next_tuple.index(biggest_possible)
        
if __name__ == "__main__":
    triangle = [
        (75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (95, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (17, 47, 82, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (18, 35, 87, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (20, 4, 82, 47, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (19, 1, 23, 75, 3, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (88, 2, 77, 73, 7, 63, 67, 0, 0, 0, 0, 0, 0, 0, 0),
        (99, 65, 4, 28, 6, 16, 70, 92, 0, 0, 0, 0, 0, 0, 0),
        (41, 41, 26, 56, 83, 40, 80, 70, 33, 0, 0, 0, 0, 0, 0),
        (41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 0, 0, 0, 0, 0),
        (53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 0, 0, 0, 0),
        (70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 0, 0, 0),
        (91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 0, 0),
        (63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 0),
        (4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23)
        ]
    print(maximum_path_sum(triangle))