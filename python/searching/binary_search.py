from typing import List, Optional


class BinarySearch:
    def binary_search_recursive(numbers: List[int], target: int, start: int, end: int) -> Optional[int]:
        """
        Recursive implementation of binary search.
        In addition to the list of numbers and target, the start and end pointer must be given,
        corresponding to the portion of the list that should be searched.
        The initial call to binary_search_recursive should have start == 0 and end == len(numbers) - 1,
        meaning that binary search should search the whole list of numbers.
        """
        # If start > end, means that target does not exist within the numbers list
        # Note start == end condition does not work for the edge case where target is the final element in the list
        if start > end:
            return None

        midpoint = (start + end) // 2
        if target == numbers[midpoint]:
            # Found target number
            return midpoint
        elif target < numbers[midpoint]:
            return BinarySearch.binary_search_recursive(numbers, target, start, midpoint)
        else:
            return BinarySearch.binary_search_recursive(numbers, target, midpoint + 1, end)

    def binary_search_iterative(numbers: List[int], target: int) -> Optional[int]:
        """
        Iterative implementation of binary search
        """
        left = 0
        right = len(numbers) - 1

        while left <= right:
            midpoint = (left + right) // 2
            if target == numbers[midpoint]:
                return midpoint
            elif target < numbers[midpoint]:
                right = midpoint
            else:
                left = midpoint + 1

        return
