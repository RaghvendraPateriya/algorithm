"""
=========================
Sliding window Technique
=========================

Problem Type: Find the subarray of maximum sum.

Example:
--------

array             = 2, 3, 5, 2, 9, 7, 1
size of sub array = 3 
output            = 18 (sum of subarray [9, 7, 1])

Explanation:
------------

arrays of size 3
2, 3, 5 => 10(sum)
3, 5, 2 => 10
5, 2, 9 => 16
2, 9, 7 => 18
9, 7, 1 => 17


Solution:
---------

1. Brute Force : 
2. Optimized - Sliding Window Technique 

Type:
-----
1. Fixed window size: Subarray size is given.
2. Variable window size: Find the Subarray size based on some condition for example based on given sum.

Test Case:
----------

1. On Empty list/array should return empty.

>>> print(get_maximum_sub_array_brute_force([], 3))

2. on empty or negative subarray size retun origin array.

>>> print(get_maximum_sub_array_brute_force([1,2,3,4], -1))

3. Subarray size is equal to array size.

>>> print(get_maximum_sub_array_brute_force([1,2,3,4], 4))

"""


def get_maximum_sub_array_brute_force(arr: list, k:int) -> list:
  
    max = 0
    sub_array = list()
    
    if k <= 0 or k is None:
        return arr
    if not arr:
        return
    
    for i in range(0, len(arr)):
        sub_array_sum = 0
        if i+k > len(arr):
            break
        for j in range(i, i+k):
            #print(arr[j] , end=',')
            sub_array_sum += arr[j]
        if max < sub_array_sum:
            max = sub_array_sum
            sub_array = arr[i:j+1]
    return max, sub_array


def get_maximum_sub_array_optimized(arr: list, k: int) -> list:

    max_sum = sum(arr[0:k])
    sub_array = arr[0:k]
    
    if not arr:
        return
    if k is None or k <= 0:
        return arr
    
    for i in range(1, len(arr)):
        if i+k >= len(arr):
            break
        sub_array_sum = max_sum - arr[i-1] + arr[i+k-1]
        if max_sum < sub_array_sum:
            max_sum = sub_array_sum
            sub_array = arr[i:i+k]
    return max_sum, sub_array



if __name__ == '__main__':
    arr = [2, 3, 5, 2, 9, 7, 1]
    k = 3 # subarray size
    # Brute Force technique
    # print(get_maximum_sub_array_brute_force(arr, k))

    # Optimized Technique
    # print(get_maximum_sub_array_optimized(arr, k))
    # print(get_maximum_sub_array_optimized([], 3))
    print(get_maximum_sub_array_optimized([1,2,3,4,5,6], None))
    
