"""
Flatten binary tree.

Solution:
 - Time complexity: O(n)
 - Space complexity: O(h)
"""


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def flatten_tree(root):
    if root is None:
        return
    else:
        flatten_tree(root.left)
        flatten_tree(root.right)
        right_subtree = root.right
        root.right = root.left
        root.left = None
        temp = root
        while temp.right is not None:
            temp = temp.right
        temp.right = right_subtree


tree = Tree(
    data=4,
    left=Tree(data=6, left=Tree(data=3), right=Tree(data=5)),
    right=Tree(data=7, left=Tree(1), right=Tree(2))
)

print(flatten_tree(tree))
