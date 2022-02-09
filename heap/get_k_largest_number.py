"""
Find the kth largest element in a number stream
Design a class to efficiently find the Kth largest element in a stream of numbers. The class should have the following two things:​

The constructor of the class should accept an integer array containing initial numbers from the stream and an integer K.

The class should expose a function add(int num) which will store the given number and return the Kth largest number.

Example:

Input: [4, 1, 3, 12, 7, 14], K = 3
1. Calling add(6) should return '7'.
2. Calling add(13) should return '12'.
2. Calling add(4) should still return '12'.

"""

import heapq

class KthLargestNumber:
  minHeap = []
  
  def __init__(self, nums, k):
    
    self.k = k
    for num in nums:
      self.add(num)

  def add(self, num):
     heapq.heappush(self.minHeap, num)
     

     if len(self.minHeap) > self.k:
       heapq.heappop(self.minHeap)
     return self.minHeap[0]

if __name__ == '__main__':
  obj = KthLargestNumber([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(obj.add(6)))
  print("4th largest number is: " + str(obj.add(13)))
  print("4th largest number is: " + str(obj.add(4)))
