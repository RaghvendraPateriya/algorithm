"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

def merge_interval(intervals: list[list[int]])-> list[list[int]]:

    # First we sort the interval based on first value
    intervals.sort(key=lambda interval: interval[0])

    # merged the overlaped intervals
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            # here 2 condition we are checking
            # 1. if first element merged list empty
            # 2. non overlaping interval by merged[-1][1] < interval[0] last endi of merge less then next interval of start
            merged.append(interval)
        else:
            # here we are updating the last interval
            merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
    return merged

    # Time complexity : O(n log n) because of sorting
    # Space: O(1), we are doing in place sorting, we don't count the output merged list    
    
        

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
print(merge_interval([[1,3],[2,6],[8,10],[15,18]]))

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
print(merge_interval([[1,4],[4,5]]))

