class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, l, r = -1,0, len(matrix) - 1

        while l <= r:
            mid = (l+r) // 2

            if matrix[mid][0] <= target:
                row = mid
                l = mid + 1
            else:
                r = mid - 1
        
        if row == -1:
            return False
        
        l,r = 0, len(matrix[0])-1

        while l <= r:
            mid = (l+r) // 2
            if matrix[row][mid] == target:
                return True
            
            if matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

