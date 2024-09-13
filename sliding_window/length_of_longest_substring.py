"""
Longest substring with out the repeting character.
Given a string s, find the length of longest substring without repecting character.

Example: 1
-----------

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example: 2
----------

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example: 3
----------

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Solutions:
----------

This problem solved by the Sliding Window Algorithm.

Setp:
1. As per the sliding window, we have two pointer left & Right
2. We don't focus on right pointer since we have a condition (unique character)
3. Store the left pointer in start_indx variable
4. for character uniquness store the char in dict like {a: 1, b:2, c:1}
5. loop over each character
    5.1 if char not in dict update the max lenght
    5.2 else char in dict, update the start_indx
    5.3 calcualte the max length by using max function:
        max(previous_length, current_length)
        previous_length we store in max_lenght var
        current_lenght we calcualte by : i-start_indx+1


"""

from collections import Counter

def length_of_longest_substring(s: str) -> int:
  char_indx_dict = {}
  start_indx = 0
  max_lenght = 0

  for i, char in enumerate(s):
    # check if char in char_indx_dict and i >= start_indx
    if char in char_indx_dict and i>=start_indx:
      start_indx = char_indx_dict[char] + 1 # update the left pointer to current index
    else:
      max_lenght = max(max_lenght, i-start_indx+1)

    char_indx_dict[char]=1
  return max_lenght

# Test Case
s1 = "abcabcbb" # 3
s2 = "bbbbb" # 1
s3 = "pwwkew" # 3
print(length_of_longest_substring(s3))
