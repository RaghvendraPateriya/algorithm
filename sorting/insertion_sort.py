"""
Insertion Sort Algorithm.

Complexity:

0(n^2) Worst case
0(n^2) Average Case
0(n)   Best Case

Space Complexity: 0(n)


Example:

Input: [34, 21, 12, 1, 100, 67, 32, 34]

Output: [1, 12, 21, 32, 34, 34, 67, 100]


Psudo Code:
==========

A = [a1, a2, a3 ... an]

for j to A.length:
    key = A[j] // Insert A[j] into sorted sequence a[1, j-1]
    i = j - 1
    while i>0 and A[i]>key:
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key


Findings:
    #1 if input array is sorted then it will be `Liner Function`.
    #2 if input array in decreasing order then it would be `Quadratic Function`.
    #3 Not good for larger array
    #4 Stable, Online, In-Place, Simple Implementation
    #5 Insertion sort is less efficient then QuickSort, HeapSort, MergeSort for large data set
"""


input_list = [34, 21, 12, 1, 100, 67, 32, 34]

print('Input Array: ', input_list)

for j in range(1, len(input_list)):
    key = input_list[j]
    i = j - 1
    while i>=0 and input_list[i]>key:
        input_list[i+1] = input_list[i]
        i = i - 1
    input_list[i+1] = key 

print('Output Array: ', input_list)