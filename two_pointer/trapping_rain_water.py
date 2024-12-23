"""
trapping-rain-water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Dig: https://leetcode.com/problems/trapping-rain-water/description/
 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

def trap(heights: list[int]) -> int:
    left_wall = 0 # left wall always 0
    right_wall = 0 # Right wall always 0
    max_lenght = len(heights)
    left_max = [0] * max_lenght
    right_max = [0] * max_lenght
   
    # we are creating two list left and right
    # left_max will hold the max hight for left side at point(index) Forward directed
    # right_max will hold the max hight for right side point(index)  Reverse Direction
    for i in range(max_lenght):
        j = -i -1
        left_max[i] = left_wall
        right_max[j] = right_wall
        left_wall = max(left_wall, heights[i])
        right_wall = max(right_wall, heights[j])
    
    summ = 0
    for i in range(max_lenght):
        pos = min(left_max[i], right_max[i])
        summ += max(0, pos - heights[i])
    
    return summ

print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # Output 6