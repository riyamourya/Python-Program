def merge_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list

def interchange_first_last(list):
    if len(list) >= 2:
        list[0], list[-1] = list[-1], list[0]
    return list

def find_even_numbers(list):
    even_numbers = [num for num in list if num % 2 == 0]
    return even_numbers

def is_ascending(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

# Example usage
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = merge_lists(list1, list2)
print("Merged List:", merged_list)

list = [7, 8, 9, 10, 11]
interchanged_list = interchange_first_last(list)
print("Interchanged List:", interchanged_list)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = find_even_numbers(list)
print("Even Numbers:", even_numbers)

list = [1, 2, 3, 4, 5]
is_ascending_order = is_ascending(list)
print("Ascending Order:", is_ascending_order)
