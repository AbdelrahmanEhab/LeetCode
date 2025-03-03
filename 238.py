from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r = [1], 1

        for i in range(len(nums) - 1):
            l.append(l[-1] * nums[i])

        for i in range(len(nums) - 1, -1, -1):
            l[i] = l[i] * r
            r = r * nums[i]
        
        return l

        # Time Complexity : o(n)
        # Space Complexity : o(n)