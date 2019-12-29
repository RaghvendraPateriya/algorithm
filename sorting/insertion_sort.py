"""
Insertion Sort Algorithm.

Complexity: n^2

Input: [34, 21, 12, 1, 100, 67, 32, 34]

Output: [1, 12, 21, 32, 34, 34, 67, 100]


Psudo Code:
==========


A = [a1, a2, a2 ... an]

for j to A.lenght:
    key = A[j] // Insert A[j] into sorted sequence a[1, j-1]
    i = j - 1
    while i>0 and A[i]>key:
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key


Findings:
    #1 if input array is sorted then it will be `Liner Function`.
    #2 if input array in decreasing order then it would be `Quadratic Function`.
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