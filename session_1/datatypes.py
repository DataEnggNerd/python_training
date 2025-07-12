"""
Module for basic datatypes
"""

# simple datatype

string_dtype: str = "Manish Dave" # string datatype

number_dtype: int = 1234

float_dtype: float = 123.010

bool_dtype: bool = False

# complex datatypes

list_dtype: list[str|int] = ["Manish", "Dave", 123, 456, [1, 2, 3]]

dict_dtype: dict[str, str] = {"first_name": "Manish", "last_name": "Dave", "meta": {"age": 50}} 

tuple_dtype: tuple[int] = (1, 2, 3, [1, 2, 3]) # immutable datatype

set_dtype: set[int] = {1, 2, 3}

duplicate_list: list[int] = [1,2,2,4,4,5,5,5,5,5,5,3]

deduplicated_set: set[int] = set(duplicate_list) # deduplication and sorts elements of a list


# mutable datatype in a immutable datatype stays mutable
inner_list = tuple_dtype[-1]
inner_list.append(4)

# shallow copy 
first_list: list[str] = ["a", "b", "c"]
second_list: list[str] = first_list
second_list.append("d")

# Todo 1 - Find the solution for prevention of shallow copy

# important datatype in Python

none_dtype: None = None

print(dict_dtype.get("first_name").upper())
print(dict_dtype.get("employment", "").upper())

first_list_element = list_dtype[0]
print(first_list_element)

# non returning functions
employment = list_dtype.append("advarisk")
print(employment) # retunrs nothing
print(list_dtype) # modified list



