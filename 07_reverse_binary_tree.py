"""
Given a binary tree of integers root, create a function that reverses
it left to right in-place.

Solution:
 - Time complexity: O(n)
 - Space complexity: O(h)
"""


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def show_tree(self):
        if self.left:
            self.left.show_tree()
        print(self.data, end=' '),
        if self.right:
            self.right.show_tree()


def reverse_binary_tree(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    reverse_binary_tree(root.left)
    reverse_binary_tree(root.right)


tree = Tree(
    data=4,
    left=Tree(data=6, left=Tree(data=3), right=Tree(data=5)),
    right=Tree(data=7, left=Tree(1), right=Tree(2))
)
tree.show_tree()
print('\n')
reverse_binary_tree(tree)
tree.show_tree()
