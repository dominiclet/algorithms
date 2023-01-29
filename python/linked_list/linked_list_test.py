from linked_list import LinkedList

test_list = [1, 5, 10, 25, 343, 234, 4, 0, 94]


def test_create_linked_list():
    linked_list = LinkedList(test_list)
    # Test that head and tail of linked list is correct
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 94
    curr_node = linked_list.head
    for i in range(len(test_list)):
        assert curr_node.value == test_list[i]
        curr_node = curr_node.next
    # Test that final node should point to nothing
    assert curr_node is None


def test_find_midpoint():
    linked_list = LinkedList(test_list)
    assert linked_list.midpoint().value == 343


def test_append():
    linked_list = LinkedList(test_list)
    linked_list.append(123123)
    # Verify that tail points to newly appended element
    assert linked_list.tail.value == 123123
    # Verify that the final element is indeed the newly appended element
    prev = None
    curr = linked_list.head
    while curr is not None:
        prev = curr
        curr = curr.next
    assert prev.value == 123123
