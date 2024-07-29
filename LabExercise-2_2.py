from typing import Set, List

def add_element(s: Set[int], element: int) -> Set[int]:
    """Add an element to the set, ensuring no errors if the element is already present."""
    s.add(element)
    return s

def remove_element(s: Set[int], element: int) -> Set[int]:
    """Remove an element from the set, ensuring no errors if the element is not present."""
    s.discard(element)
    return s

def union_and_intersection(set1: Set[int], set2: Set[int]) -> tuple[(Set[int], Set[int])]:
    """Return the union and intersection of two sets, handling empty sets correctly."""
    union = set1.union(set2)
    intersection = set1.intersection(set2)
    return union, intersection

def difference(set1: Set[int], set2: Set[int]) -> Set[int]:
    """Return the difference S1−S2, handling empty sets correctly."""
    return set1.difference(set2)

def is_subset(set1: Set[int], set2: Set[int]) -> bool:
    """Check if set S1 is a subset of set S2, handling empty sets correctly."""
    return set1.issubset(set2)

def set_length(s: Set[int]) -> int:
    """Find the length of a set without using the len() function."""
    length = 0
    for _ in s:
        length += 1
    return length

def symmetric_difference(set1: Set[int], set2: Set[int]) -> Set[int]:
    """Compute the symmetric difference of two sets."""
    return set1.symmetric_difference(set2)

def power_set(s: Set[int]) -> Set[Set[int]]:
    """Compute the power set of a given set."""
    power_set_result = set()
    power_set_result.add(frozenset())  # Start with the empty set
    for element in s:
        new_subsets = set()
        for subset in power_set_result:
            new_subset = subset.union({element})
            new_subsets.add(new_subset)
        power_set_result.update(new_subsets)
    # Convert frozensets back to sets
    return {set(subset) for subset in power_set_result}

def unique_subsets(s: Set[int]) -> List[Set[int]]:
    """Get all unique subsets of a given set."""
    power_set_result = power_set(s)
    return list(power_set_result)

def display_menu():
    print("\n--- Set Operations Menu ---")
    print("1. Add element to set")
    print("2. Remove element from set")
    print("3. Union and Intersection of two sets")
    print("4. Difference between two sets")
    print("5. Check if one set is a subset of another")
    print("6. Find the length of a set")
    print("7. Symmetric difference between two sets")
    print("8. Power set of a set")
    print("9. Unique subsets of a set")
    print("10. Exit")

def main():
    set1 = set()
    set2 = set()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ")
        
        if choice == '1':
            element = int(input("Enter element to add to Set 1: "))
            set1 = add_element(set1, element)
            print(f"Updated Set 1: {set1}")
        
        elif choice == '2':
            element = int(input("Enter element to remove from Set 1: "))
            set1 = remove_element(set1, element)
            print(f"Updated Set 1: {set1}")
        
        elif choice == '3':
            print("Set 1:", set1)
            print("Set 2:", set2)
            union, intersection = union_and_intersection(set1, set2)
            print(f"Union: {union}")
            print(f"Intersection: {intersection}")
        
        elif choice == '4':
            print("Set 1:", set1)
            print("Set 2:", set2)
            diff = difference(set1, set2)
            print(f"Difference (Set 1 - Set 2): {diff}")
        
        elif choice == '5':
            print("Set 1:", set1)
            print("Set 2:", set2)
            result = is_subset(set1, set2)
            print(f"Is Set 1 a subset of Set 2? {'Yes' if result else 'No'}")
        
        elif choice == '6':
            print("Set 1:", set1)
            length = set_length(set1)
            print(f"Length of Set 1: {length}")
        
        elif choice == '7':
            print("Set 1:", set1)
            print("Set 2:", set2)
            sym_diff = symmetric_difference(set1, set2)
            print(f"Symmetric difference: {sym_diff}")
        
        elif choice == '8':
            print("Set 1:", set1)
            p_set = power_set(set1)
            print(f"Power set of Set 1: {p_set}")
        
        elif choice == '9':
            print("Set 1:", set1)
            u_subsets = unique_subsets(set1)
            print(f"Unique subsets of Set 1: {u_subsets}")
        
        elif choice == '10':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()
