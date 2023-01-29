from merge_sort import MergeMethod, MergeSort
from bubble_sort import BubbleSort
from test_data import tests


def test_merge_sort():
    merge_sort = MergeSort()
    for test in tests:
        result = merge_sort.run(test["unsorted"])
        assert result == test["sorted"]


def test_merge_sort_concise():
    merge_sort = MergeSort(MergeMethod.ListPop)
    for test in tests:
        result = merge_sort.run(test["unsorted"])
        assert result == test["sorted"]


def test_simple_bubble_sort():
    for test in tests:
        result = BubbleSort.bubble_sort_simple(test["unsorted"])
        assert result == test["sorted"]


def test_bubble_sort():
    for test in tests:
        result = BubbleSort.bubble_sort(test["unsorted"])
        assert result == test["sorted"]
