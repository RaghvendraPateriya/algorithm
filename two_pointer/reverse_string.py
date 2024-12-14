"""
Reverse the Input array 
    * s.reverse()
    * s[::-1]
    * Using Two Pointer

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""

def reverseString(s: list[str]) -> list:
        """
        Do not return anything, modify s in-place instead.
        """
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer <= right_pointer:
            s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
            left_pointer +=1
            right_pointer -=1

s = ["h","e","l","l","o"]
s1 = ["H","a","n","n","a","h"]
reverseString(s1)
print(s1)