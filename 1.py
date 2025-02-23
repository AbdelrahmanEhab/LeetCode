from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i, num in enumerate(nums):
            s[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in s and s[diff] != i:
                return [i, s[diff]]
        
        return []

        # Time Complexity: O(n)
        # Space Complexity: O(n)