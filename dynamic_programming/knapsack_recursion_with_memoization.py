"""
0-1 Knapsack using recurison with memoization. 

Using Two dimension matrix to store(memoize) the result of overlapping sub problem.

"""

def memoize():
    # Create a matrix
    # Constraints 0<n<100 & 0<m<100
    return [[-1 for j in range(100)] for i in range(100)]

def knapsack_recursion_with_memoization(weight, values, capacity, item):
    if item == 0 or capacity == 0:
        return 0
    if matrix[item][capacity] != -1:
        return matrix[item][capacity]
    if weight[item - 1] <= capacity:
        matrix[item][capacity] = max(value[item - 1] + knapsack_recursion_with_memoization(
            weight, values, capacity - weight[item - 1], item - 1),
                   knapsack_recursion_with_memoization(weight, values, capacity, item - 1))
        return matrix[item][capacity]
    elif weight[item - 1] > capacity:
        matrix[item][capacity] = knapsack_recursion_with_memoization(weight, values, capacity, item - 1)
        return matrix[item][capacity]


# Driver Code
if __name__ == '__main__':
    value = [120, 100, 60]
    weight = [10, 20, 30]
    capacity = 50
    matrix = memoize()
    print(knapsack_recursion_with_memoization(weight, value, capacity, 3))
    
