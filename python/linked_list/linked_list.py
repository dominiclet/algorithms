from __future__ import annotations
from typing import List, Optional


class ListNode:
    """
    Each ListNode contains the value of the element and a pointer to the next ListNode.
    """
    def __init__(self, value: any, next: Optional[ListNode] = None):
        self.value = value
        self.next = next


class LinkedList:
    """
    A LinkedList is a combination of ListNodes. Here, we store first ListNode,
    ie. the head of the linked list, so we can traverse the linked list.
    We also store the last ListNode, ie. the tail of the linked list,
    so that more elements can be added in O(1) time.
    """
    def __init__(self, values: List):
        self.head = ListNode(values[0])
        prev = self.head
        for value in values[1:]:
            prev.next = ListNode(value)
            prev = prev.next
        self.tail = prev

    def midpoint(self) -> ListNode:
        """
        Find midpoint of the linked list using the "tortoise and hare" method.
        Maintain two pointers at the start of the list. The first pointer traverses the linked list
        one node at a time while the second pointer traverses two nodes at a time.
        When the second pointer finishes traversing the linked list, the first pointer will be at the midpoint.
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def append(self, value: any):
        """
        To append to list, make tail of linked list point to the newly created ListNode element.
        Then update the new tail of the linked list as the new ListNode.
        """
        self.tail.next = ListNode(value)
        self.tail = self.tail.next
