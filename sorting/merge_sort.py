"""
MergeSort

Based on Devide & Conquer Technique.

Complexity:
-----------
Time  : O(nlogn)
Space : 
"""


def merge(left, right):
  sorted_arr = [] 
  i = 0
  j = 0
  while i<len(left) and j<len(right):
    if left[i] < right[j]:
      sorted_arr.append(left[i])
      i+=1
    else:
      sorted_arr.append(right[j])
      j+=1
  while i<len(left):
      sorted_arr.append(left[i])
      i+=1
  while j<len(right):
      sorted_arr.append(right[j])
      j+=1
    
  return sorted_arr

def merge_sort(arr):
  if len(arr) == 1:
    return arr
  mid = len(arr)//2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  return merge(left, right)

if __name__ == '__main__':
  arr = [1, 10, 30, 4, 8, 6]
  print(f'Sorted: {merge_sort(arr)}') 
