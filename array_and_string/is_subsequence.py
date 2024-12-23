"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
"""

def isSubsequence(s: str, t: str) -> bool:
        s_list = list(s) # ['a', 'b', 'c']
        indx = 0
        if len(s) == 0: 
            return True
        if len(t) == 0:
            return False
        for char in t: #'ahbgdc'
            if char == s_list[indx]:
                indx += 1
            if indx == len(s_list):
                return True
        return False

# print(isSubsequence('abc', 'ahbgdc'))
print(isSubsequence('', 'ahbgdc'))
