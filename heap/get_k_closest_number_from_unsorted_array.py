"""
Find k closest numbers in an unsorted array

Input:
 k = 3 # Number of return
 x = 7 # Target Element
 muns = [5, 7, 6, 9, 8]

 Explain
 abs(nums - x)
 5    - 7 = 2
 7    - 7 = 0
 6    - 7 = 1
 9    - 7 = 2
 8    - 7 = 1

Result = 7, 6, 8

Complexity: O(n logk)
"""

import heapq


class KClosestNumber:

    def __init__(self, k, nums, x):
        self.k = k
        self.x = x
        self.minHeap = nums

    def get_closest_elements(self):
        return heapq.nsmallest(self.k, self.minHeap, key=lambda num: abs(num - self.x))


if __name__ == '__main__':
    obj = KClosestNumber(3, [5, 7, 6, 9, 8], 7)
    print(obj.get_closest_elements())
