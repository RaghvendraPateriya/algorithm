"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""

def is_palindrome(s: str) -> bool:
    
    if len(s.strip()) == 1:
        return True
    alphanum_s = []
    # Remove all space and special character 
    for i in s:
        if i.isdigit():
            alphanum_s.append(i)
        if i.isalpha():
            alphanum_s.append(i.lower()) # lower the case
    # Use two pointer to validate the list
    left_pointer = 0
    right_pointer = len(alphanum_s) - 1
    while left_pointer < right_pointer:
        if alphanum_s[left_pointer] == alphanum_s[right_pointer]:
            left_pointer += 1
            right_pointer -=1
        else:
            return False
    return True

#  print(is_palindrome('race a car')) # False
print(is_palindrome("A man, a plan, a canal: Panama")) # True
    