"""
Sort linked list.
(merge sort)

Solution:
 - Time complexity: O(n*logn)
 - Space complexity: O(logn)
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head


def merge_sorted_lists(head1, head2):
    ptr1 = head1
    ptr2 = head2
    returned_head = None
    tail = None
    while ptr1 or ptr2:
        if ptr1 and ptr2:
            if ptr1.data < ptr2.data:
                lower = ptr1
                ptr1 = ptr1.next_node
            else:
                lower = ptr2
                ptr2 = ptr2.next_node
        elif ptr1:
            lower = ptr1
            ptr1 = ptr1.next_node
        else:
            lower = ptr2
            ptr2 = ptr2.next_node
        if returned_head is None:
            returned_head = lower
            tail = lower
        else:
            tail.next_node = lower
            tail = tail.next_node
    return returned_head


def merge_sort(head):
    if head is None or head.next_node is None:
        return head
    slow = head
    fast = head
    while fast.next_node and fast.next_node.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
    head_right_half = slow.next_node
    slow.next_node = None
    head = merge_sort(head)
    head_right_half = merge_sort(head_right_half)
    return merge_sorted_lists(head, head_right_half)


def sort_list(lst):
    lst.head = merge_sort(lst.head)


node5 = Node(4, next_node=None)
node4 = Node(1, next_node=node5)
node3 = Node(2, next_node=node4)
node2 = Node(3, next_node=node3)
node1 = Node(5, next_node=node2)
test_linked_list = LinkedList(node1)

print(test_linked_list.head.data)
print(test_linked_list.head.next_node.data)
print(test_linked_list.head.next_node.next_node.data)
print(test_linked_list.head.next_node.next_node.next_node.data)
print(test_linked_list.head.next_node.next_node.next_node.next_node.data)
sort_list(test_linked_list)
print(test_linked_list.head.data)
print(test_linked_list.head.next_node.data)
print(test_linked_list.head.next_node.next_node.data)
print(test_linked_list.head.next_node.next_node.next_node.data)
print(test_linked_list.head.next_node.next_node.next_node.next_node.data)
