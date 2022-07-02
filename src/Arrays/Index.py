# 283. Move Zeroes
import math


def move_zeros(numbers=[0, 1, 0, 3, 12]):
    # send all non zero integers to the front of the array
    j = 0
    n = len(numbers)

    for num in numbers:
        if num != 0:
            numbers[j] = num
            j += 1

    # set the rest to 0s
    for x in range(j, n):
        numbers[x] = 0

# print(move_zeros())


# 881. Boats to Save People
def num_rescure_boats(people=[1, 2, 3], limit=3):
    """ 
    Maximize the num od pair of people whose weight can be added together
    in the same boat... ie: the sum of the weight <= input limit.

    Algorithms:
    - sort the array
    - add the heaviest and light person in a boat, using the 2 pointer technique
    """
    people.sort()
    left = 0
    right = len(people) - 1
    boats_num = 0

    while left <= right:
        if left == right:
            boats_num += 1
            break

        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats_num += 1

    return boats_num


# print(num_rescure_boats())


# 941. Valid Mountain Array

def valid_array(arr=[0, 3, 2, 1]):
    """ Find if an array contains an increasing, then decreasing subarrays """
    if len(arr) < 3:  # min num for a valid mountain array
        return False

    i = 1

    while i < len(arr) and arr[i] > arr[i + 1]:
        i += 1
    if i == 1 or i < len(arr):
        return False
    while i < len(arr) and arr[i] < arr[i - 1]:
        i += 1

    return i == len(arr)


# print(valid_array())

# 11. Container With Most Water
"""
Find two containers using the coordinates such that they hold the max amount of water
finding two lines that can contain the most water
find the max difference btw x position multiplied by the height

we try to maximize our answer
by finding min btw the two buildings being pointed ay by our pointers
then multiply that by the distace between the two buildings
"""


def max_area(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]):

    left = 0
    right = len(height) - 1
    max_diff = 0

    while left < right:
        max_diff = max(max_diff, min(
            height[left], height[right]) * (right - left))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_diff


# print(max_area())


# 278. First Bad Version
"""
Return the first bad version of a product
Algorithm:
create two pointers
find mid b/w the 2 pinters
if mid !bad, start = mid + 1, else, end = mid
"""


def first_bad_version(n=10, isBadVersion=3):

    left = 1
    right = n - 1
    first_bad_v = range(1, n + 1)
    mid = (left + right) // 2

    while left < right:

        if isBadVersion(first_bad_v[mid]):
            right = mid

        else:
            left = mid + 1

    return right + 1


# print(first_bad_version())

# 3. Longest Substring Without Repeating Characters
"""
Two pointers, each
create a hash table 
have a ans val

"""


def length_of_longest_substring(string="abcabcbb"):

    hash_map = {}

    left = 0
    right = 0
    ans = 0
    n = len(string)

    while left < n and right < n:
        el = string[right]

        if el in hash_map:
            # set count to max and update pointer pos
            left = max(left, hash_map[el] + 1)

        hash_map[el] = right
        ans = max(ans, right - left + 1)
        right += 1

    return ans


# print(length_of_longest_substring())

# 34. Find First and Last Position of Element in Sorted Array
"""
Two pointers, right and left
create mid : is there a element of the same kind that comes before?
if yes, reduce the left count 
"""


class Solution:
    def get_left_pos(self, num, target):

        left = 0
        right = len(num) - 1

        while left <= right:
            mid = (left + right) // 2
            if num[mid] == target:
                if mid - 1 >= 0 and num[mid - 1] != target or mid == 0:
                    return mid
                right = mid - 1
            elif num[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return - 1

    def get_left_pos(self, num, target):

        left = 0
        right = len(num) - 1
        mid = (left + right) // 2

        while left <= right:
            if num[mid] == target:
                if mid + 1 >= 0 and num[mid + 1] == target or mid == 0:
                    return mid
                left = mid + 1
            elif num[mid] > target:
                left = mid + 1
            else:
                right = mid - 1
        return - 1

    def first_and_last_pos(self, num, target):
        left = self.get_left_pos(num, target)
        right = self.get_right_pos(num, target)

    # print(get_left_pos())


# 268. Missing Number
def missing_number(num=[0, 1, 4, 2, 5]):

    n = len(num)
    current_sum = sum(num)
    indended_sum = n * (n + 1) / 2

    return int(indended_sum - current_sum)


# print(missing_number())

# 204. Count Primes


def count_prime(n):

    if n < 2:
        return 0

    primes = [True] * n
    primes[0] = primes[1] = False

    for num in range(2, n):
        if primes[num]:
            primes[2 * num:n:num] = [False] * ((n-1) // num - 1)

    return sum(primes)


# print(count_prime(10))


# 136. Single Number
def single_num(input=[2, 2, 1]):

    return 2 * sum(set(input)) - sum(input)

# print(single_num())


# 657. Robot Return to Origin
def judge_circle(moves):
    x = 0
    y = 0

    for move in moves:
        if move == "U":
            y += 1
        if move == "R":
            x += 1
        if move == "D":
            y -= 1
        if move == "L":
            x -= 1
    return x == 0 and y == 0


# print(judge_circle("UD"))


# 67. Add Binary
def add_binary(a="11", b="1"):

    carry = 0
    result = []
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total % 2))
        carry = total // 2

    return ''.join(reversed(result))


print(add_binary())
