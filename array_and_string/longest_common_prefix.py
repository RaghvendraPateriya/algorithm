"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.


"""

def longestCommonPrefix(strs: list[str]) -> str:
    # First we ge the min length of string
    min_length = float('inf')
    for str in strs:
        if len(str) < min_length:
            min_length = len(str)
    # Now we are loop over the strs with min_lenth time check the prefix
    i = 0
    while i < min_length:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]
        i +=1
    return strs[0][:i]
       
print(longestCommonPrefix(["flower","flow","flight"]))

print(longestCommonPrefix(["dog","racecar","car"]))