class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1

# Example usage:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Input: nums = [2,0,1]
# Output: [0,1,2]

solution = Solution()
nums1 = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums1)
print(nums1)
nums2 = [2, 0, 1]
solution.sortColors(nums2)
print(nums2)

