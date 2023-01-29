from typing import List


class BubbleSort:
    @staticmethod
    def bubble_sort_simple(numbers: List) -> List:
        """
        Idea is to "bubble" the greatest element to the front.
        After N times of "bubbling", we are guaranteed with a sorted list.
        """
        numbers_len = len(numbers)
        for _ in range(numbers_len):
            for i in range(numbers_len - 1):
                # If element is greater than the next element, swap places
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        # Returning numbers is optional as we sorted numbers in-place
        return numbers

    @staticmethod
    def bubble_sort(numbers: List) -> List:
        """
        Since we know that the n greatest elements to the right must be sorted after n rounds of "bubbling",
        we don't need to bubble for the last n elements.
        Hence, we can "bubble" up to the nth element, then (n-1)th element, then (n-2)th element, and so on.
        """
        for i in range(len(numbers), -1, -1):
            for j in range(i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return numbers
