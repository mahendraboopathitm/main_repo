# Python Program Demonstrating All Major Data Types

# 1. Numeric Types
int_num = 10          # Integer
float_num = 3.14      # Float
complex_num = 2 + 3j  # Complex Number

# 2. Sequence Types
string_val = "Hello, Python!"     # String
list_val = [1, 2, 3, "Alice"]    # List
tuple_val = (10, 20, "Bob")      # Tuple
range_val = range(5)             # Range

# 3. Mapping Type
dict_val = {"name": "Alice", "age": 20, "grade": "A"}  # Dictionary

# 4. Set Types
set_val = {1, 2, 3, 3, 4}         # Set (duplicates removed)
frozenset_val = frozenset([1, 2, 3])  # Frozenset (immutable set)

# 5. Boolean Type
bool_val = True   # Boolean

# 6. None Type
none_val = None   # NoneType

# Printing Values and Their Types
print( "| Type:", type(int_num))
print("Float:", float_num, "| Type:", type(float_num))
print("Complex:", complex_num, "| Type:", type(complex_num))
print("String:", string_val, "| Type:", type(string_val))
print("List:", list_val, "| Type:", type(list_val))
print("Tuple:", tuple_val, "| Type:", type(tuple_val))
print("Range:", list(range_val), "| Type:", type(range_val))  # Convert range to list for display
print("Dictionary:", dict_val, "| Type:", type(dict_val))
print("Set:", set_val, "| Type:", type(set_val))
print("Frozenset:", frozenset_val, "| Type:", type(frozenset_val))
print("Boolean:", bool_val, "| Type:", type(bool_val))
print("NoneType:", none_val, "| Type:", type(none_val))
