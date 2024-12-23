"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
----------------------------------------------------------------------------------
 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

"""

from math import ceil

def test_k_works(k_hour: int, target_hours: int, banana_piles: list)-> bool:
    hour_sum = 0
    for i in banana_piles:
        hour_sum += ceil(i / k_hour)
    return hour_sum <= target_hours
    

def find_k(target_hours: int, banana_piles: list)-> int:

    left_p = 1
    right_p = max(banana_piles)

    while left_p < right_p:

        mid_p = (left_p + right_p) // 2
        if test_k_works(mid_p, target_hours, banana_piles):
            right_p = mid_p
        else:
            left_p = mid_p + 1
    return right_p

# Test Case - 1
# Input: piles = [3,6,7,11], h = 8
# Output: 4
print(find_k(8, [3,6,7,11]))