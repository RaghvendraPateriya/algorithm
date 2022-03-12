"""
Jump Search: Is kind of Binary search, to check fewer element (than Linear Search) by jumpping ahead by fixed step
or skipping some element in place of searching all elements.

Optimal Block size for Jump:  roo(n)

Complexity: 
Time: 0(square root of n)

Important points: 
 

1. Works only sorted arrays.
2. The optimal size of a block to be jumped is (√ n). This makes the time complexity of Jump Search O(√ n).
3. The time complexity of Jump Search is between Linear Search ( ( O(n) ) and Binary Search ( O (Log n) ).
4. Binary Search is better than Jump Search, but Jump search has an advantage that we traverse back only once
   (Binary Search may require up to O(Log n) jumps, consider a situation where the element to be searched is the
   smallest element or just bigger than the smallest). So in a system where binary search is costly, we use Jump Search.

"""
from cmath import sqrt


def jump_search(arr, search_term):

    if not arr:
        return -1

    arr_size = len(arr)
    jump_block_size = int(sqrt(arr_size).real)
    
    start_indx = 0
    end_indx = 0
    found = False

    if arr[start_indx] == search_term:
        return start_indx

    for i in range(start_indx, arr_size, jump_block_size):
        if arr[i] == search_term:
            return i

        if arr[i] > search_term:
            start_indx = i - jump_block_size
            end_indx = i
            break
   
    for j in range(start_indx, end_indx):
        if arr[j] == search_term:
            found = True
            return j
    if not found:
        return -1


# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 5, 8, 12, 45, 60]
    # arr = []
    # arr = [1]
    print(jump_search(arr, 12))