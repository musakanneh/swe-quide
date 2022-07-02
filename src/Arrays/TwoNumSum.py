class Solution(object):
    def twoNumberSum(self, array, targetSum):
        array.sort()
        left = 0
        right = len(array) - 1

        while left < right:
            current_sum = array[left] + array[right]
            if current_sum == targetSum:
                return [array[left], array[right]]
            elif current_sum < targetSum:
                left += 1
            elif current_sum > targetSum:
                right -= 1

        return []


inputs = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10
# print(Solution().twoNumberSum(inputs, target_sum))

# Three num sum


class Solution(object):
    def threeNumberSum(self, array, targetSum):
        array.sort()
        tripplets = []

        for i in range(len(array) - 2):
            left = i + 1
            right = len(array) - 1

            while left < right:
                current_sum = array[i] + array[left] + array[right]
                if current_sum == targetSum:
                    tripplets.append([array[i], array[left], array[right]])
                    left += 1
                    right += 1
                elif current_sum < targetSum:
                    left += 1
                elif current_sum > targetSum:
                    right -= 1
        return tripplets


inputs = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
print(Solution().threeNumberSum(inputs, targetSum))
