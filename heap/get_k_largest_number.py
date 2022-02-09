import heapq

class KLargestNumber:

  def __init__(self, nums, k):
    self.heap = []
    self.k = k
    for num in nums:
      self.add(num)

  def add(self, num):
     heapq.heappush(self.heap, num)

     if len(self.heap) > self.k:
       heapq.heappop(self.heap)
     return self.heap[0]

if __name__ == '__main__':
  obj = KLargestNumber([4, 1, 3, 12, 7, 14], 3)
  print(f'3 rd largest number: {obj.add(6)}')