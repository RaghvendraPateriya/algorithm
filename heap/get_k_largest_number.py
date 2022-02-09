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
     print(f'adding num {self.minHeap}')
     return self.minHeap[0]

if __name__ == '__main__':
  obj = KthLargestNumber([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(obj.add(6)))
  print("4th largest number is: " + str(obj.add(13)))
  print("4th largest number is: " + str(obj.add(4)))