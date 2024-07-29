

from typing import List
import statistics

def find_max_value(lst: List[int]) -> int:
    """Return the maximum value in the list."""
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

def find_min_value(lst: List[int]) -> int:
    """Return the minimum value in the list."""
    if not lst:
        raise ValueError("List is empty")
    return min(lst)

def calculate_sum(lst: List[int]) -> int:
    """Return the sum of all elements in the list."""
    return sum(lst)

def compute_average(lst: List[int]) -> float:
    """Return the average of the list."""
    if not lst:
        raise ValueError("List is empty")
    return sum(lst) / len(lst)

def determine_median(lst: List[int]) -> float:
    """Return the median of the list."""
    if not lst:
        raise ValueError("List is empty")
    return statistics.median(lst)

# Example usage
if __name__ == "__main__":
    # Create lists using Python comprehension
    list1 = [i for i in range(1, 11)]  # List of integers from 1 to 10
    list2 = [i for i in range(10, 0, -1)]  # List of integers from 10 to 1
    list3 = [5, 2, 9, 1, 5, 6]  # List with some random integers

    # Demonstrate the use of each function
    print(f"List 1: {list1}")
    print(f"Maximum value: {find_max_value(list1)}")
    print(f"Minimum value: {find_min_value(list1)}")
    print(f"Sum of elements: {calculate_sum(list1)}")
    print(f"Average of elements: {compute_average(list1)}")
    print(f"Median of elements: {determine_median(list1)}")

    print("\nList 2: {list2}")
    print(f"Maximum value: {find_max_value(list2)}")
    print(f"Minimum value: {find_min_value(list2)}")
    print(f"Sum of elements: {calculate_sum(list2)}")
    print(f"Average of elements: {compute_average(list2)}")
    print(f"Median of elements: {determine_median(list2)}")

    print("\nList 3: {list3}")
    print(f"Maximum value: {find_max_value(list3)}")
    print(f"Minimum value: {find_min_value(list3)}")
    print(f"Sum of elements: {calculate_sum(list3)}")
    print(f"Average of elements: {compute_average(list3)}")
    print(f"Median of elements: {determine_median(list3)}")
