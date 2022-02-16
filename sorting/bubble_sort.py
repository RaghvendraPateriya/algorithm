"""
Bubble Sort

Time Complexity :

Worst Case: 0(n^2)
Best Case: 0(n)

Space Complexity: 0(1)

Example

Input:  [1, 6, 4, 5]
Output: [1, 4, 5, 6]

"""

def bubble_sort(elements):

    current_indx = 0
    while True:
        swap = False
        if current_indx >= len(elements) -1:
            break
        for i in range(current_indx, len(elements)):
            if i+1 >= len(elements):
                break
            if elements[i] > elements[i+1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]
                swap = True
        if not swap:
            current_indx += 1

# using second loop
# you can use this to sort strings too
def bubble_sortv2(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    tests = [
        [5, 9, 2, 1, 67, 34, 88, 34],
        [1, 2, 3, 4, 2],
        ["mona", "dhaval", "aamir", "tina", "chang"]
    ]
    for elements in tests:
        bubble_sort(elements)
        print(elements)


