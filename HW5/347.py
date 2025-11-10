import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = Counter(nums)

        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in sorted(heap, key=lambda x: x[0], reverse=True)]
    

# Example 1: Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2: Input: nums = [1], k = 1
# Output: [1]

# Example 3: Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]

Sol = Solution()
print(Sol.topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
print(Sol.topKFrequent([1], 1))  # [1]
print(Sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))  # [1,2]