"""
Square of sorted array

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


"""

def get_square_of_sorted_array(input_array: list)-> list:
    left_pointer = 0
    right_pointer = len(input_array) - 1
    result = []

    while left_pointer <= right_pointer:
        if abs(input_array[left_pointer]) > abs(input_array[right_pointer]):
            result.append(abs(input_array[left_pointer]**2))
            left_pointer +=1
        else:
            result.append(abs(input_array[right_pointer]**2))
            right_pointer -=1
    result.reverse()
    return result

array = [-7,-3,2,3,11]
print(get_square_of_sorted_array(array))