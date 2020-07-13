# 根据题意进行bfs广度优先搜索。 假如碰到的是数字，直接修改后返回，否则要统计上下左右加上斜的四个方向，共八个方向，相邻也包括斜的。

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        boar=[]
        for i in board:
            x = []
            for j in i:
                x.append(j)
            boar.append(x)
        if not boar or not boar[0]:
            return board
        
        x, y = click[0], click[1]
        if boar[x][y] == "M":# dig into the mine, you can modify it directly and then return
            boar[x][y] = "X"
            new_board = []
            for i in boar:
                new_board.append("".join(j for j in i))
            return new_board
        
        m, n = len(boar), len(boar[0])
        visited = [[0 for _ in range(n + 1)] for j in range(m + 1)]

        dx = [1, 1, -1, -1, 0, 0, -1, 1]
        dy = [1, 0, -1, 0, 1, -1, 1, -1]
        
        def dfs(x0, y0):
            if boar[x0][y0] == "M" or visited[x0][y0] == 1: #If the point is a mine or has already arrived, return directly
                return
                                               
            visited[x0][y0] = 1 #Mark it over.
            mineCnt = 0         #Calculate several mines near the current point
            for k in range(8):
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x < m and 0 <= y < n and board[x][y] == "M":
                    mineCnt += 1
            
            if mineCnt > 0:
                boar[x0][y0] = str(mineCnt) #If there is a mine, it is said that there are several mines.
            else:
                boar[x0][y0] = 'B' #Without adjacent mines, you need to recursively around the point

                for k in range(8):
                    x = x0 + dx[k]
                    y = y0 + dy[k]

                    if 0 <= x < m and 0 <= y < n and visited[x][y] == 0:
                        dfs(x, y)

        dfs(x, y)

        new_board = []
        for i in boar:
            new_board.append("".join(j for j in i))
        return new_board