class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
             return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    islands += 1

        return islands                    

    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        grid[x][y] = '0'
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y):
                    continue
                queue.append((next_x, next_y))
                grid[next_x][next_y] = '0'

    def is_valid(self, grid, x, y):         
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y] == '1'


算法思路： 两层for循环按行列遍历题目所给的数组，当遍历点值为1时，答案值（岛屿数量）加一，然后从这个点开始bfs，搜索所有与其相连的点。将当前点推入队列，每次从取出队头点(x,y)，将(x,y)的上下左右四个方向中所有合法点（坐标合法且值为1）推入队列，推入队列时将点数值改为0以标记已走过该点，当队列为空时，遍历结束。

代码思路：
function bfs(x,y) //从x,y点出发开始搜索
    queue.push(x,y) //将当前点推入队列
    map[x][y] = 0 //走过的点赋值为0
    while(!queue.empty())//当队列为空则结束循环
        (now_x,now_y) = queue.front()
        queue.pop() //将队头元素取出
        for i 1:4 //遍历四个方向
            next_x = now_x + dir[i][0] //得到下一个位置坐标
            next_y = now_y + dir[i][1]
            if(0<=next_x<n && 0<=next_y<m && map[next_x][next_y]==1)
            //合法性判断
                map[next_x][next_y] = 0  //走过的点赋值为0，以便不会再次遍历
                queue.push(next_x,next_y) //将该点推入队列
时间复杂度：O(n*m)
n为行数，m为列数，显然，每个值为1的点都会被遍历一次