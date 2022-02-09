"""
MergeSort

Based on Devide & Conquer Technique.

Complexity:
-----------
Time  : O(nlogn)
Space : 
"""

def merge_sort(arr):
  if len(arr) <= 1:
    retutn arr
  mid = len(arr)//2
  left = merge_sort(arr[0:mid])
  right = merge_sort(arr[mid])
  return merge(left, right)

def merge(left, right):
  sorted_arr = []
  i, j = 0
  while i<len(left) and j<len(right):
    if left[i] < right[j]:
      sorted_arr.append[i]
    else:
      sorted_arr.append[j]
    while i<len(left):
      sorted_arr.append[i]
    while j<len(right):
      sorted_arr.append[j]
  retun sorted_arr
      
if __name__ == '__main__':
  arr = [1, 10, 30, 4, 8, 6]
  print(f'Sorted: {merge_sort(arr)}) 
