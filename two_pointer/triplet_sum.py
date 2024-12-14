"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""

def get_3_sum(array: list, target_sum: int)-> list[list]:
    hasmap = {}
    array_length = len(array)
    result = set()

    for indx, elem in enumerate(array):
        hasmap[elem] = indx
    
    for i in range(array_length):
        for j in range(i+1, array_length):
            # two_sum = array[i] + array[j]
            desired = -array[i] -array[j] # this need to remember
            if desired in hasmap and hasmap[desired] != i and hasmap[desired] != j:
                result.add(tuple(sorted([array[i], array[j], desired])))
    print(result)

get_3_sum([-1,0,1,2,-1,-4], 0)