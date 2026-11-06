class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        t = row * col
        l, r = 0, t-1

        while l <= r:
            mid = (l+r)//2
            mid_i = mid//col
            mid_j = mid%col
            mid_element = matrix[mid_i][mid_j]

            if mid_element < target:
                l = mid + 1
            elif mid_element > target:
                r = mid - 1
            else:
                return True
        
        return False