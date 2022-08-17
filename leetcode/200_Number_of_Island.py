class Solution(object):
    def dfs(self, x, y):

        if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid[0]):
            return False

        if self.grid[x][y] == "1":
            # 방문한 결과로 0 으로 초기화
            self.grid[x][y] = " 0"

            # 상하좌우 확인
            self.dfs(x - 1, y)
            self.dfs(x + 1, y)
            self.dfs(x, y - 1)
            self.dfs(x, y + 1)
            return True  # 연결된 곳 모두 방문하였으면 True

        return False
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.cnt = 0
        self.grid = grid



        result = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.dfs(i, j):  # 탐색 결과가 True면
                    self.cnt += 1

        return self.cnt


print(Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
