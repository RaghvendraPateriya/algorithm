"""
Basic Recursion Example

Find the sum form 1-> 5 using recursion.

Examples : https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""


# USing for loop
def find_sum():
    sum = 0
    for i in range(6):
        sum += i
    return sum


def find_sum_using_recurssion(i):
    if i == 1:
        return 1
    return i + find_sum_using_recurssion(i - 1)


# 1 Write a Python program to calculate the sum of a list of numbers.
def get_sum(elems, i):
    if i == 0:
        return elems[i]
    return elems[i] + get_sum(elems, i - 1)


def get_sum_v2(elems):
    if len(elems) == 1:
        return elems[0]
    return elems[0] + get_sum_v2(elems[1:])


# 2 Write a Python program to converting an Integer to a string in any base.
def to_string(number, base):
    convert_string = '0123456789ABCDEF'
    if number < base:
        return convert_string[number]
    return to_string(number // base, base) + convert_string[number % base]


# 3 Write a Python program of recursion list sum
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21
def get_recursive_sum(numbers):
    total = 0
    for num in numbers:
        if isinstance(num, list):
            total = total + get_recursive_sum(num)
        else:
            total = total + num
    return total


# 4  Write a Python program to get the factorial of a non-negative integer
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)


# 5 Write a Python program to solve the Fibonacci sequence using recursion
def fab(n):
    if n == 0 or n == 1:
        return n
    return fab(n - 1) + fab(n - 2)


# 6 Write a Python program to get the sum of a non-negative integer
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9
def get_integer_digit_sum(number):
    if number == 0:
        return 0
    return number % 10 + get_integer_digit_sum(number // 10)


# 7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0). Go to the editor
# Test Data:
# sum_series(6) -> 12
# sum_series(10) -> 30
def sum_series(num):
    if num - 2 == 0:
        return num
    return num + sum_series(num - 2)


# 8. Write a Python program to calculate the harmonic sum of n-1.
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# Example :
# 1 + 1/2 + 1/3 + 1/4 ...
# harmonic series
def harmonic_series_sum(n):
    if n == 1:
        return n
    return 1/n + harmonic_series_sum(n-1)


# 9. Write a Python program to calculate the geometric sum of n-1.
# Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.
# Example :
def geometric_sum(n):
    if n < 0:
        return 0
    else:
        return 1 / (pow(2, n)) + geometric_sum(n - 1)


# 10. Write a Python program to calculate the value of 'a' to the power 'b'. Go to the editor
# Test Data : (power(3,4) -> 81
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)


# 11. Write a Python program to find the greatest common divisor (gcd) of two integers.
def get_gcd(a, b):  # Euclid Algorithm
    if a == b:
        return a
    if a > b:
        return get_gcd(a-b, b)
    else:
        return get_gcd(a, b-a)


def get_gcd_optimized(a, b):  # Euclidean Algorithm
    low = min(a, b)
    high = max(a, b)

    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return get_gcd_optimized(low, high%low)


if __name__ == '__main__':
    # print(find_sum())
    # print(find_sum_using_recurssion(5))
    # print(get_sum([1, 2, 3, 4], 3))
    # print(get_sum_v2([1, 2, 3, 4]))
    # print(to_string(2835, 16))
    # print(get_recursive_sum([1, 2, [3, 4], [5, 6]]))
    # print(factorial(5))
    # print(fab(7))
    # print(get_integer_digit_sum(345))
    # print(sum_series(10))
    # print(harmonic_series_sum(4))
    # print(geometric_sum(7))
    # print(geometric_sum(4))
    # print(power(3, 4))
    print(get_gcd(30, 18))