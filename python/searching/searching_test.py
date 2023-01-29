from linear_search import LinearSearch
from binary_search import BinarySearch

test_list = [123, 452, -123, 0, -333, 12, 4, 1923, 29, 323]


def test_linear_search():
    for i, number in enumerate(test_list):
        assert i == LinearSearch.linear_search(test_list, number)

    # Test non-existent number
    assert LinearSearch.linear_search(test_list, 1002309202) is None


def test_binary_search_recursive():
    sorted_test_list = sorted(test_list)
    for i, number in enumerate(sorted_test_list):
        assert i == BinarySearch.binary_search_recursive(sorted_test_list, number, 0, len(sorted_test_list) - 1)

    # Test non-existent number
    assert BinarySearch.binary_search_recursive(sorted_test_list, 1234567, 0, len(sorted_test_list) - 1) is None


def test_binary_search_iterative():
    sorted_test_list = sorted(test_list)
    for i, number in enumerate(sorted_test_list):
        assert i == BinarySearch.binary_search_iterative(sorted_test_list, number)

    # Test non-existent number
    assert BinarySearch.binary_search_iterative(sorted_test_list, 1234567) is None
