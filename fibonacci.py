"""
Print the  Fibonacci Series till nth element.

Input: n = 5
Output: 0 1 1 2 3 5

"""

def get_fibonacci_series(n):
  result_list = []
  current_element = 0
  next_element = 1
  counter = 0
  result_list.append(current_element)
  result_list.append(next_element)
  while(counter<=n-2):
    current_element, next_element = next_element, current_element + next_element
    result_list.append(next_element)
    counter += 1
  return  result_list

print(get_fibonacci_series(5))
