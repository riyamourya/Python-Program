def sum_of_tuple_elements(t):
    return sum(t)

def sort_tuples_alphabetically(tuples_list):
    return sorted(tuples_list, key=lambda x: x[0])

def check_element_in_tuple(element, t):
    return element in t

tuple1 = (5, 10, 15, 20)
print("Tuple:", tuple1)
print("Sum of tuple elements:", sum_of_tuple_elements(tuple1))

tuples_list = [("John", 25), ("sonu", 20), ("harshita", 30), ("rohan", 22)]
print("\nTuples List:", tuples_list)
print("Sorted tuples alphabetically:", sort_tuples_alphabetically(tuples_list))

tuple2 = ("apple", "banana", "orange", "grape")
print("\nTuple:", tuple2)
element = "banana"
print(f"Is '{element}' present in the tuple? {check_element_in_tuple(element, tuple2)}")
