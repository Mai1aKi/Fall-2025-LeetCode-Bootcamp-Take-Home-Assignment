from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        while q:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

        return minutes if fresh == 0 else -1


Sol = Solution()

# Example 1:
grid1 = [[2,1,1],[1,1,0],[0,1,1]]
print(Sol.orangesRotting(grid1))  # 4

# Example 2:
grid2 = [[2,1,1],[0,1,1],[1,0,1]]
print(Sol.orangesRotting(grid2))  # -1

# Example 3:
grid3 = [[0,2]]
print(Sol.orangesRotting(grid3))  # 0