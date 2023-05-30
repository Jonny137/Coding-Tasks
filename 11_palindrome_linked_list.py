"""
Check if linked list is a palindrome.

Solution:
 - Time complexity: O(n)
 - Space complexity: O(1)
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head


def reverse_list(head):
    previous = None
    current = head
    while current is not None:
        next_node = current.next_node
        current.next_node = previous
        previous = current
        current = next_node
    return previous


def is_palindrome(linked_list):
    slow = fast = linked_list.head
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
    slow = reverse_list(slow)
    head = linked_list.head
    while slow:
        if slow.data != head.data:
            return False
        slow = slow.next_node
        head = head.next_node
    return True


node4 = Node('a', next_node=None)
node3 = Node('b', next_node=node4)
node2 = Node('b', next_node=node3)
node1 = Node('a', next_node=node2)
test_linked_list = LinkedList(node1)
print(is_palindrome(test_linked_list))
