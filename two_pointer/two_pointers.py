"""
* 
* Two pointer aprroach to reduce the complexity from O(n^2) to O(n)
* we have a sroted array to find the two elements sum is equal to given value
*
Input: [1,2,3,4,5]
sum: 6
5 & 1  
"""

def get_two_sum(input_list, target_sum):

    left_pointer = 0
    right_pointer = len(input_list)-1

    while left_pointer <= right_pointer:
        elem_sum = sum([input_list[left_pointer] + input_list[right_pointer]])

        if elem_sum == target_sum:
            return input_list[left_pointer], input_list[right_pointer]
        
        if elem_sum < target_sum:
            left_pointer += 1
        else:
            right_pointer -=1
    return 'Not Found'

list_1 = [1,2,3,4,5, 6]
print(get_two_sum(list_1, 8))