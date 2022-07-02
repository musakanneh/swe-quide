# Given an array of integers of size n, where all elements
# are between 1 and n inclusive, find all of the elements of [1, n]
# that do not appear in the array. Some numbers may appear more than once.
#  -----------------------------------------------------------------------
# Input: [4, 5, 2, 6, 8, 2, 1, 5]
# Output: [3, 7]


class Solution(object):
    def findDisappearedNumbers(self, inputs):
        
        inputs.sort()
        left, right = 0, 0
        missing_num = 0

        for i in range(len(inputs)):
            n = left[i] + right[i + 1] // 2
            if n >= 2:
                n = missing_num
                return missing_num
            inputs[left[i]] += 1

        return inputs


inputs = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumbers(inputs))

