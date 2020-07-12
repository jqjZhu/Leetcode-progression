#解题思路
#通过树上节点的相对位置，我们可以对树节点进行编号，左节点的列编号值是当前节点的列编号减一，右节点的列编号是当前节点的列编号加一。通过一次深度优先或宽度优先遍历，就可以得到这些节点的列编号。

#如果用深度优先遍历将列编号按遍历顺序加入答案结果，可能会导致，同一列的数组中节点的编号没有按照节点深度排序。所以采用宽度优先搜索更优秀，可以按深度将同一列节点按顺序加入数组。

#采用深度优先遍历也可行，但是要多记录节点的深度，最后将答案将深度排序，会增加程序的复杂度。

# 代码思路
# 将(root, 0)加入队列，这个元组代表节点，和该结点的列编号。
# 取出队首元素，令(node, colIdx)为当前遍历到的节点和列编号。
# 如果node为空，跳到第2步。
# 将node.val加入对应colIdx的数组。
# 将(node.left, colIdx - 1)加入队列。
# 将(node.right, colIdx + 1)加入队列。
# 如果队列非空，跳到第2步，否则结束程序。
# 统计结果。
# 复杂度分析
# 设二叉树的节点数为N。

# 时间复杂度
# 宽度优先遍历的时间复杂度为O(N)。
# 用于存放结果的map或dict根据其实现方式不同而不同，如果是Java的Treeset，c++的map，时间复杂度为O(NlogN)。python的dict复杂度为O(N)，对于key的排序，时间复杂度为O(NlogN)。
# 总时间复杂度为O(NlogN)。
# 空间复杂度
# 记录结果的Map或dict的空间复杂度为O(N)。
# 宽度优先遍历的空间复杂度为O(N)。
# 总的空间复杂度为O(N)。

# Using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists:

# >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# >>> d = defaultdict(list)
# >>> for k, v in s:
# ...     d[k].append(v)
# ...
# >>> d.items()
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

# Setting the default_factory to int makes the defaultdict useful for counting (like a bag or multiset in other languages):

# >>> s = 'mississippi'
# >>> d = defaultdict(int)
# >>> for k in s:
# ...     d[k] += 1
# ...
# >>> d.items()
# [('i', 4), ('p', 2), ('s', 4), ('m', 1)]

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        results = collections.defaultdict(list)
        queue = collections.deque()
        
        queue.append((root, 0))
        # 宽度优先遍历，同时记录列编号
        while queue:
            node, col_idx = queue.popleft()
            if node:
                results[col_idx].append(node.val)
                queue.append((node.left, col_idx - 1))
                queue.append((node.right, col_idx + 1))
        
        return [results[i] for i in sorted(results)]