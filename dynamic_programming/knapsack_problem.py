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
  
  if item == 0 or weight > capacity:
    return 0
  
  return max( kanpsack(weight, value, capacity-weight[items-1], items-1),
             kanpsack(weight, value, capacity, items-1))
             
