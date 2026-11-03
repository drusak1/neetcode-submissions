class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

            
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        perimeter += 1
                    elif grid[nr][nc] == 0:
                        perimeter += 1
        return perimeter
