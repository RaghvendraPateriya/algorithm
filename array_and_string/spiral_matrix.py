"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
[
    [1 ->2 -> 3]
              |
    [4 ->5 ->6]
     ^
     |       |
    [7 <-8 <-9]
]

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

"""
def sprial_metrics(matrix: list[list[int]]) -> list[int]:
    """
    1. We need to print/add the wall of the metrics in each iteration
    2. Walls RIGHT -> DOWN -> UP -> TOP and repeat
    3. The loop breaking condition : row * column <= result[], 
       all member of matrics to be added in result output array
    """
    row, col = len(matrix), len(matrix[0])
    result = []
    RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3, 4  # Directions
    direction = RIGHT # this will keep track of movement of direction
    i, j = 0, 0 # initial index of matrics
    while len(result) <= row*col: # m*n
        if direction == RIGHT:
            if j < col:
                result.append(matrix[i][j])
                j +=1
            i, j = i+1, j-1
            direction = DOWN

        if direction == DOWN:
            if i < row:
                result.append(matrix[i][j])
                i +=1
            i, j = i-1, j-1
            direction = LEFT

        if direction == LEFT:
            if j < col:
                result.append(matrix[i][j])
                j = j-1
            i, j = i-1, j+1
            direction = UP

        else:
            if i < row:
                result.append(matrix[i][j])
                i = i-1
            i, j = i+1, j
            direction = RIGHT

    