from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}

        for num in nums:
            s[num] = 1 + s.get(num, 0)

        s = sorted(s.items(), key=lambda x: x[1])
        res = []

        for i in range(k):
            res.append(s[len(s) - 1 - i][0])

        return res

        # Time Complexity: o(nlogn)
        # Space Complexity: o(n)

        