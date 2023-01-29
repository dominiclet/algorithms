from typing import List, Optional


class LinearSearch:
    @staticmethod
    def linear_search(numbers: List[int], target: int) -> Optional[int]:
        for i, number in enumerate(numbers):
            if number == target:
                return i
