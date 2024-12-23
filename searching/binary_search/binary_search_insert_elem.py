"""

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""
def searchInsert(nums: list[int], target: int) -> int:
        left_p = 0
        right_p = len(nums) -1

        while left_p <= right_p:
            mid = left_p + (right_p-left_p) // 2

            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left_p = mid +1
            else:
                right_p = mid -1
        if nums[mid] < target:
             return mid+1
        else: 
             return mid

lst = [1,3,5,6]
target = 10
print(searchInsert(lst, target)) # 4

lst1 = [1,3]
target = 2
print(searchInsert(lst1, target)) # 1

# lst1 = [2,3]
# target = 1
# print(searchInsert(lst1, target)) # 0