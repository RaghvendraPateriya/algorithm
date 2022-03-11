"""
Binary search: search element in sorted array.

Step-by-step Binary Search Algorithm: We basically ignore half of the elements just after one comparison.

#1 Compare x with the middle element.
#2 If x matches with the middle element, we return the mid index.
#3 Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for the right half.
#4 Else (x is smaller) recur for the left half.

Time Complexity: 0(logn)

"""

def binary_search(arr, start_indx, end_indx, element):
    
    if start_indx <= end_indx:

        mid_element_indx = start_indx + (end_indx - start_indx) // 2

        if arr[mid_element_indx] == element:
            return mid_element_indx

        elif arr[mid_element_indx] > element: # left side search
            return binary_search(arr, start_indx, mid_element_indx-1, element)
        else:
            return binary_search(arr, mid_element_indx+1, end_indx, element)
    else:
        return -1

# Driver Code
if __name__ == '__main__':
    arr = [2, 5, 8, 12, 50, 80, 100]
    result = binary_search(arr, 0, len(arr)-1, 80)
    print(result)

