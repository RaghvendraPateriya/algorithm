"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.

Test Case-I
-----------

Input:[ [1,1,1],
        [1,0,1],
        [1,1,1]
      ]

Output:[ [1,0,1],
         [0,0,0],
         [1,0,1]
      ]

Test Case- II
------------
Input:[ [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
      ]

Output:[ [0,0,0,0],
         [0,4,5,0],
         [0,3,1,0]
      ]

---------
Solution:
---------
We are using the first row & column as markers.
If we find any element is zero then we mark the corresponding first row & column element as zero.
in next loop we will mark all element zero based on markers row/coulmn.

One special case:
if we find any element is zero in the first row & column we need to mark all elements zero.
"""

def set_metrics_row_column_zero(metrics: list(list))-> list(list):
  m = len(metrics) # row count
  n = len(metrics[0] # column count
  first_row_marker_zero = false
  first_column_marker_zero = false

  # Check if first row or column is zero
  for i in range(0, m):
    if metrics[i][0]==0:
      first_row_marker_zero=True
      break
  for j in range(0, n):
    if metrics[0][j]==0:
      first_column_marker_zero=True

  # check if the internal element is zero and mark the corresponding first row/column element zero
  for i in range(0, m):
    for j in range(0, n):
      if metrics[i][j]==0:
        metrics[i][0]=0
        metrics[0][j]=0

  # based on first row/column mark all element zero
  for i in range(0, m):
    for j in range(0, n):
    if metrics[i][0]==0 or metircs[0][j]==0
      metrics[i][j]=0
  
  # Mark first row/column zero is zero markers are set to true
  if first_row_marker_zero:
    for i in range(0, m):
      metrics[i][0]=0

  if first_column_marker_zero:
    for j in range(0, n):
      metrics[0][j]=0
  

