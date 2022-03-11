"""
Linear Search is a sequential search,  In this, the list or array is traversed sequentially and every element is checked.

Time Complexity: 0(1) to 0(n) based of searched element position.

"""

def linear_search(arr, elem):

    if not arr:
        return 'Empty list/array'
    for indx, val  in enumerate(arr):
        if val == elem:
            return indx
    else:
        return 'Not Found'


if __name__ == '__main__':
    arr = [1, 4, 3, 5, 2, 6, 0]
    print(linear_search(arr, 4)) # return the index

