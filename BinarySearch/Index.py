import math
# LeetCode: 704. Binary Search


def binary_search(arr=[1, 2, 3, 4, 5], target=4):

    left = 0
    right = len(arr) - 1

    while (left <= right):
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return - 1


# print(binary_search())

# 69. Sqrt(x)

# class Solution:
def s_root(x=4):
    # return math.sqrt(x)

    low = 0
    high = x // 2

    while (low <= high):
        mid = low + (high - low) // 2

        if (mid ** 2 < x):
            low = mid + 1

        elif(mid ** 2 > x):
            high = mid - 1

        else:
            return mid

    return high


print(s_root())


# 350. Intersection of Two Arrays II
