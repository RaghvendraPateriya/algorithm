"""
Print the  Fibonacci Series till nth element.

Input: n = 5
Output: 0 1 1 2 3 5

"""

def get_fibonacci_series(nth_term):
    result_list = []
    current_element = 0
    next_element = 1
    counter = 0
    result_list.append(current_element)
    result_list.append(next_element)

    if nth_term <= 0:
        return "Please enter positive number"
    if nth_term == 1:
        return current_element

    while (counter < nth_term - 2):
        current_element, next_element = next_element, current_element + next_element
        result_list.append(next_element)
        counter += 1
    return result_list

  
# Driver Code
if __name__ == '__main__':
    print(get_fibonacci_series(3))
    #print(get_fibonacci_series(0))
    #print(get_fibonacci_series(-1))
    #print(get_fibonacci_series(1)) 
