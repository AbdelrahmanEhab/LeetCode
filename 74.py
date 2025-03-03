from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        l, r = 0, R*C - 1

        while l <= r:
            c = (l+r) // 2
            row, col = c // C, c % C

            if target == matrix[row][col]:
                return True

            elif target > matrix[row][col]:
                l = c + 1
            else:
                r = c - 1

        return False 
        