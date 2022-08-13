"""

0-1 Kanpsack problem 

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack

Input:

Weight:
Value:
Capacity:

Output: Maximum weight
"""

def knapsack(weight, value, capacity, items):

    # Base condition
    if items == 0 or capacity == 0:
        return 0
    # Choices
    if weight[items-1] <= capacity:
        return max(value[items-1] + knapsack(weight, value, capacity-weight[items-1], items-1),
                   knapsack(weight, value, capacity, items-1))
    elif weight[items-1] > capacity:
        return knapsack(weight, value, capacity, items - 1)


# Driver Code
if __name__ == '__main__':
    value = [60, 100, 120]
    weight = [10, 20, 30]
    capacity = 50
    print(knapsack(weight, value, capacity, 3))
