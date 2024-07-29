# main_ListOperations.py

import module_ListFunction as mlf

def display_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("1. Find the maximum value in a list")
    print("2. Find the minimum value in a list")
    print("3. Calculate the sum of elements in a list")
    print("4. Compute the average of a list")
    print("5. Determine the median of a list")
    print("6. Exit")

def get_list_input():
    """Get a list of integers from the user."""
    try:
        lst = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
        return lst
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return get_list_input()

def main():
    while True:
        display_menu()
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            lst = get_list_input()
            print("Max:", mlf.find_max(lst))
        elif choice == '2':
            lst = get_list_input()
            print("Min:", mlf.find_min(lst))
        elif choice == '3':
            lst = get_list_input()
            print("Sum:", mlf.calculate_sum(lst))
        elif choice == '4':
            lst = get_list_input()
            print("Average:", mlf.compute_average(lst))
        elif choice == '5':
            lst = get_list_input()
            print("Median:", mlf.compute_median(lst))
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
