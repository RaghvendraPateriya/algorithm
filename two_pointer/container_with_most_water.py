"""

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
  Y
  |
8-|    |              |
7-|    |              |     |
6-|    |  |           |     |
5-|    |  |     |     |     |
4-|    |  |     |  |  |     | 
3-|    |  |     |  |  |  |  | 
2-|    |  |  |  |  |  |  |  |
1-|_|__|__|__|__|__|__|__|__|______ X

Example 1:
----------

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case,
the max area of water (blue section) the container can contain is 49.

Example 2:
----------
Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""
def get_max_area(nums: list) -> int:
    width = len(nums) # lenght of array is width
    left_pointer = 0
    right_pointer = width - 1
    max_area = 0

    while left_pointer < right_pointer:
        if left_pointer == right_pointer:
            left_pointer +=1
        currenet_area = min(nums[left_pointer], nums[right_pointer]) * (right_pointer - left_pointer)
        if max_area < currenet_area:
            max_area = currenet_area
        
        if left_pointer > right_pointer:
            right_pointer -=1
        else:
            left_pointer +=1
        
    return max_area

print(get_max_area([1,8,6,2,5,4,8,3,7]))


