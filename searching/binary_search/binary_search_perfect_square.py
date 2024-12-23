"""
A Valid Perfect Square

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

"""

def isPerfectSquare(num: int) -> bool:
        left_p = 1
        right_p = num //2

        if num == 1 or num == 0:
            return True

        while left_p <= right_p:
            mid = (left_p + right_p) // 2
            squr = mid*mid
            if squr == num:
                return True
            if squr > num:
                right_p = mid-1
            else:
                left_p = mid +1
        return False