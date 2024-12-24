"""
Rotate array by K

Example:
Input = [1,2,3,4,5,6,7], k=3
Output: [7,6,5,1,2,3]

Rotate k = 1 : [7,1,2,3,4,5,6]
Rotate k = 2 : [6,7,1,2,3,4,5]
Rotate k = 3 : [5,6,7,1,2,3,4]

"""

def get_rotated_array(array: list[int], k ) -> list[int]:
    array_len = len(array)
    if array_len == 0:
        return array
    if k == array_len or k ==0:
        return array
    
    l1 = array[-1:-(k+1):-1]
    l2 = array[0:array_len-k:1]
    l1.reverse()
    result = l1+l2
    return result

print(get_rotated_array([1,2,3,4,5,6,7], k=3))