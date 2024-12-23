"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

def productExceptSelf(nums: list[int]) -> list[int]:
    """
    This problem we need to solve in O(n) complexity and we can't use the division operator.
    Solution:

    1. Given array: [1,2,3,4]
    2. We will define two arrays: left array and right arrray
        left_array  = [0,0,0,0]
        right_array = [0,0,0,0]
    3. we will loop over each element of array to fill the value of left_array and right array.
       3.1 left array store the multiplication of left side of each elements.
       3.2 Right array store the multiplication of right side of each elements.
    4. To get the final result we do the multipication of left and right array (index based)
        [ left_array[i]*right_array[i], left_array[j]*right_array[j]... ]
    """
    left_multiplication = 1  # considering extremen left/right would be 1
    right_multiplication = 1
    length_of_nums = len(nums)
    left_array = [0]* length_of_nums
    right_array = [0]* length_of_nums

    # Loop over each elements of nums
    for i in range(length_of_nums):
        j = -i-1 # to point reverse index to fill the right_array

        left_array[i] = left_multiplication
        right_array[j] = right_multiplication

        left_multiplication *=nums[i] 
        right_multiplication *= nums[j]
    
    return [i*j for i , j in zip(left_array, right_array)]


# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
print(productExceptSelf([1,2,3,4]))