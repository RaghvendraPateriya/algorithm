"""
Count Good String: A string having non repetative character.
Example: abd, xyz

Problem:
Find a good String.

Example:
Input
s = 'xyzzaz'
k = 3

Output: 1

Explanation:
Windows of Size k=3
xyz <- Good String
yzz
zaz

Hint: Sliding window Fixed Size wih hash.

"""

import collections

def get_good_string_count(s: str, k: int) -> int:
    result = 0
    char_count = collections.Counter()
    for i in range(len(s)):
        if i>=k:
            char_count[s[i-k]] -= 1
            if not char_count[s[i-k]]:
                del char_count[s[i-k]]
        char_count[s[i]] += 1
        if len(char_count) == k:
            result += 1
    return result

