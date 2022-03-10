"""
It is a divide and conquer approach, Where we need to find the position from where partition will happen

Note: In Place Sorting Algorithm.

for the partition we need tp first identify the pivot element:
    1. Select First element as pivot.
    2. Select last element as pivot.
    3. Select randon element as pivot.

Complexity:

Space: 0(n) 
Time: 
Best & Average: 0(nlog(n))
Worst: 0(n^2)
"""

def partition(arr, low, high):
    
    i = low -1
    j = 0
    pivot = arr[high] # We are considering the last element as a pivot

    for j in range(low, high):

        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1



def quick_sort(arr, low, high):

    if low < high:

        pi = partition(arr, low, high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


if __name__ == '__main__':
    arr = [10, 80, 30, 90, 40, 50, 70]
    quick_sort(arr, 0, len(arr)-1)
