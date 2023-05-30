"""
Tree breath first search.
By using a queue (recursively)

Solution:
 - Time complexity: O(n)
 - Space complexity: O(n)
"""


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def bfs_recursion(root, i, queue):
    if i >= len(queue):
        return
    else:
        popped_node = queue[i]
        if popped_node is not None:
            print(popped_node.data)
            queue.append(popped_node.left)
            queue.append(popped_node.right)
        bfs_recursion(root, i+1, queue)


def bfs(root):
    bfs_recursion(root, 0, [root])


tree = Tree(
    data=4,
    left=Tree(data=6, left=Tree(data=3), right=Tree(data=5)),
    right=Tree(data=7, left=Tree(1), right=Tree(2))
)

bfs(tree)
