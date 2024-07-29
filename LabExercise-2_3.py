from typing import Dict, List, Any
from collections import defaultdict

def merging_dicts(*args: Dict[Any, Any]) -> Dict[Any, Any]:
    """Merge multiple dictionaries into one. If keys are duplicated, the last dictionary's value is taken."""
    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict

def common_keys(*args: Dict[Any, Any]) -> List[Any]:
    """Find common keys in multiple dictionaries."""
    if not args:
        return []
    
    common_keys_set = set(args[0].keys())
    for d in args[1:]:
        common_keys_set &= set(d.keys())
    
    return list(common_keys_set)

def invert_dict(d: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    """Invert a dictionary, swapping keys and values. Group keys with the same value into a list."""
    inverted_dict = defaultdict(list)
    for key, value in d.items():
        inverted_dict[value].append(key)
    return dict(inverted_dict)

def common_key_value_pairs(*args: Dict[Any, Any]) -> Dict[Any, Any]:
    """Find common key-value pairs across multiple dictionaries."""
    if not args:
        return {}
    
    common_pairs = set(args[0].items())
    for d in args[1:]:
        common_pairs &= set(d.items())
    
    return dict(common_pairs)

def display_menu():
    print("\n--- Dictionary Operations Menu ---")
    print("1. Merge dictionaries")
    print("2. Find common keys in multiple dictionaries")
    print("3. Invert a dictionary")
    print("4. Find common key-value pairs across multiple dictionaries")
    print("5. Exit")

def get_dict_input(prompt: str) -> Dict[Any, Any]:
    """Helper function to get dictionary input from the user."""
    print(prompt)
    dict_str = input("Enter dictionary in the format {'key1': 'value1', 'key2': 'value2'}: ")
    try:
        return eval(dict_str)
    except (SyntaxError, ValueError):
        print("Invalid dictionary format. Using an empty dictionary.")
        return {}

def main():
    dicts = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            n = int(input("How many dictionaries do you want to merge? "))
            dicts = [get_dict_input(f"Enter dictionary {i+1}:") for i in range(n)]
            merged = merging_dicts(*dicts)
            print("Merged Dictionary:", merged)
        
        elif choice == '2':
            n = int(input("How many dictionaries to check for common keys? "))
            dicts = [get_dict_input(f"Enter dictionary {i+1}:") for i in range(n)]
            common_keys_list = common_keys(*dicts)
            print("Common Keys:", common_keys_list)
        
        elif choice == '3':
            d = get_dict_input("Enter dictionary to invert:")
            inverted = invert_dict(d)
            print("Inverted Dictionary:", inverted)
        
        elif choice == '4':
            n = int(input("How many dictionaries to check for common key-value pairs? "))
            dicts = [get_dict_input(f"Enter dictionary {i+1}:") for i in range(n)]
            common_pairs = common_key_value_pairs(*dicts)
            print("Common Key-Value Pairs:", common_pairs)
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
