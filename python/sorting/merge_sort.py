from typing import Callable, List
from enum import Enum


class MergeMethod(Enum):
    Pointer = 1
    ListPop = 2


class MergeSort:
    def __init__(self, merge_method: MergeMethod = MergeMethod.Pointer):
        self.merge_method = merge_method

    @staticmethod
    def merge_sort(numbers: List) -> List:
        """
        Recursively split list by half, then join them with merge function
        """
        # Check if base case reached (the list is halved to the point where there is only 1 element left)
        if len(numbers) == 1:
            return numbers
        # Split list by half recursively
        midpoint = len(numbers) // 2
        left = MergeSort.merge_sort(numbers[:midpoint])
        right = MergeSort.merge_sort(numbers[midpoint:])

        return MergeSort.merge(left, right)

    @staticmethod
    def merge(left: List, right: List) -> List:
        """
        Merge two lists into one sorted list.
        Since we can assume that both provided lists (left and right) are sorted,
        we can merge them in O(n+m) time, where n is len(left) and m is len(right).

        To merge, maintain two pointers for both the left and right lists, starting from the first element.
        Compare and add the lower value element to a new list. Move the pointer to the right for the list with the
        lower-valued element and repeat until all elements have been scanned for one of the list.
        Check if there are still elements remaining in the other list. If there are, we can add all of these elements
        to the end of the new list as we know that these elements must be larger than all the previously added elements.
        """
        result_list = []
        left_pointer = 0
        right_pointer = 0

        # Compare each element sequentially and add the lower of the two elements
        # until we finish adding all the elements of one of the lists.
        while left_pointer < len(left) and right_pointer < len(right):
            left_element = left[left_pointer]
            right_element = right[right_pointer]
            if left_element < right_element:
                result_list.append(left_element)
                left_pointer += 1
            else:
                result_list.append(right_element)
                right_pointer += 1

        # Add remaining values if any. At this point, only one of the lists will have any remaining values.
        while left_pointer < len(left):
            result_list.append(left[left_pointer])
            left_pointer += 1

        while right_pointer < len(right):
            result_list.append(right[right_pointer])
            right_pointer += 1

        return result_list

    @staticmethod
    def merge_concise(left: List, right: List) -> List:
        """
        More concise implementation of merge.
        Instead of using pointers, we simply pop the list until it is empty.
        Note that this implementation of merge is less efficient since each pop operation
        costs O(n) time.
        """
        result_list = []

        while left and right:
            if left[0] < right[0]:
                result_list.append(left.pop(0))
            else:
                result_list.append(right.pop(0))

        # Add remaining values if any
        while left:
            result_list.append(left.pop(0))
        while right:
            result_list.append(right.pop(0))

        return result_list

    @staticmethod
    def merge_sort_higher_order(numbers: List, merge_func: Callable[[List, List], List]) -> List:
        """
        CAN IGNORE

        Higher-order merge_sort function that accepts a merge function to be used.
        For testing different merge functions.
        """
        # Check if base case reached (the list is halved to the point where there is only 1 element left)
        if len(numbers) == 1:
            return numbers
        # Split list by half recursively
        midpoint = len(numbers) // 2
        print("SLDKJL")
        left = MergeSort.merge_sort(numbers[:midpoint])
        right = MergeSort.merge_sort(numbers[midpoint:])

        return merge_func(left, right)

    def run(self, numbers: List) -> List:
        """
        CAN IGNORE

        For testing different merge functions
        """
        if self.merge_method == MergeMethod.Pointer:
            return MergeSort.merge_sort_higher_order(numbers, MergeSort.merge)
        elif self.merge_method == MergeMethod.ListPop:
            return MergeSort.merge_sort_higher_order(numbers, MergeSort.merge_concise)
        raise Exception("Merge method not recognised")
