"""
Given a binary tree of integers root, create 3 functions
to print the elements, one for preorder, one for inorder
and one in postorder
- Preorder: Print root data, then print the left subtree then print the
            right subtree
- Inorder: Print left subtree, then print the root data then print the
           right subtree
- Postorder: Print the left subtree, then print the right subtree then print
             the root data

Solution:
 - Time complexity: O(n)
 - Space complexity: O(h)
"""


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def dfs_preorder(root):
    if root is None:
        return
    print(root.data)
    dfs_preorder(root.left)
    dfs_preorder(root.right)


def dfs_inorder(root):
    if root is None:
        return
    dfs_inorder(root.left)
    print(root.data)
    dfs_inorder(root.right)


def dfs_postorder(root):
    if root is None:
        return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.data)


tree = Tree(
    data=4,
    left=Tree(data=6, left=Tree(data=3), right=Tree(data=5)),
    right=Tree(data=7, left=Tree(1), right=Tree(2))
)

dfs_preorder(tree)
dfs_inorder(tree)
dfs_postorder(tree)
