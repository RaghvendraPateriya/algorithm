"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
(0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

def get_pivot_index(nums: list[int], target: int) -> int:

    left_p = 0
    right_p = len(nums)-1
    
    if len(nums) == 0 or len(nums) == 1:
        return -1
    
    # First we find the pivot min index then we can decide
    # in which direction we need to search
    while left_p < right_p:

        mid = (left_p+right_p)//2

        if nums[mid] > nums[right_p]:
            left_p = mid +1
        else:
            right_p = mid
    # return right_p

    # Now we got the target index
    min_index = left_p

    if nums[min_index] == 0:
        left_p = 0
        right_p = len(nums) -1
    if target > nums[0] and target < nums[min_index-1]:
        left_p = 0
        right_p = min_index
    else:
        left_p = min_index + 1
        right_p = len(nums) -1
    while left_p <= right_p:
        mid = (left_p+right_p)//2
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            left_p = mid+1
        else:
            right_p = mid -1
    return -1 


# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
print(get_pivot_index([4,5,6,7,0,1,2], 0))

#print(get_pivot_index([4,5,6,7,9,10,0,1,2], 10))