# question-1
# Complete code with functions and demonstration in one file

def find_max(lst):
    """Find the maximum value in a given list."""
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

def find_min(lst):
    """Find the minimum value in a given list."""
    if not lst:
        raise ValueError("List is empty")
    return min(lst)

def calculate_sum(lst):
    """Calculate the sum of all elements in a list."""
    if not lst:
        return 0
    return sum(lst)

def compute_average(lst):
    """Compute the average of the list."""
    if not lst:
        raise ValueError("List is empty")
    return calculate_sum(lst) / len(lst)

def compute_median(lst):
    """Determine the median of a list."""
    if not lst:
        raise ValueError("List is empty")
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def main():
    # Create lists using list comprehensions
    list1 = [x for x in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
    list3 = [x for x in range(10, 0, -1)]  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    # Use the functions on the lists
    print("List1:", list1)
    print("Max:", find_max(list1))
    print("Min:", find_min(list1))
    print("Sum:", calculate_sum(list1))
    print("Average:", compute_average(list1))
    print("Median:", compute_median(list1))

    print("\nList2:", list2)
    print("Max:", find_max(list2))
    print("Min:", find_min(list2))
    print("Sum:", calculate_sum(list2))
    print("Average:", compute_average(list2))
    print("Median:", compute_median(list2))

    print("\nList3:", list3)
    print("Max:", find_max(list3))
    print("Min:", find_min(list3))
    print("Sum:", calculate_sum(list3))
    print("Average:", compute_average(list3))
    print("Median:", compute_median(list3))

if __name__ == "__main__":
    main()
