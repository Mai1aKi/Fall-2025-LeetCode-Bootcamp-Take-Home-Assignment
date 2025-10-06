class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            
            elif current_sum < target:
                left += 1
                
            else:
                right -= 1

# Example usage:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]

# Input: numbers = [-1,0], target = -1
# Output: [1,2]

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([2, 3, 4], 6))
print(solution.twoSum([-1, 0], -1))


