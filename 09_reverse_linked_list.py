"""
Reverse linked list.

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


def reverse_list(linked_list):
    previous = None
    current = linked_list.head
    while current is not None:
        next_node = current.next_node
        current.next_node = previous
        previous = current
        current = next_node
    linked_list.head = previous


node5 = Node(4, next_node=None)
node4 = Node(1, next_node=node5)
node3 = Node(2, next_node=node4)
node2 = Node(3, next_node=node3)
node1 = Node(5, next_node=node2)
test_linked_list = LinkedList(node1)
reverse_list(test_linked_list)
print(test_linked_list.head.data)
print(test_linked_list.head.next_node.data)
print(test_linked_list.head.next_node.next_node.data)
print(test_linked_list.head.next_node.next_node.next_node.data)
print(test_linked_list.head.next_node.next_node.next_node.next_node.data)
