class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Initialize prefix and suffix product arrays with 1s
        prefix_products = [1] * len(nums)
        suffix_products = [1] * len(nums)
        result = [1] * len(nums)

        # Calculate prefix products for each index
        for i in range(1, len(nums)):
            # Multiply the previous prefix product with the previous number in nums
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
            # Calculate suffix products in reverse order
            suffix_products[len(nums) - 1 - i] = suffix_products[len(nums) - i] * nums[len(nums) - i]

        # Combine prefix and suffix products to get the result
        for i in range(len(nums)):
            result[i] = prefix_products[i] * suffix_products[i]

        return result
    
# Example usage:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))

    