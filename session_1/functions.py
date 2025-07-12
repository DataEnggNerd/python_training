"""
Module for functions or methods
"""

def function_name(parameter_1: int|str, parameter_2: int|str) -> int|str:
    """Blah blah

    Args:
        parameter_1 (int | str): _description_
        parameter_2 (int | str): _description_

    Returns:
        int|str: _description_
    """
    result = parameter_1 + parameter_2
    return result

# positional arguments
function_name(1, 2)

# named arguments or keyword arguments
# print(function_name(parameter_2="test", parameter_1="stere"))

parameters = (5, 6)
print(function_name(*parameters))

parameters_dict = {"parameter_2": 10, "parameter_1": 5}
print(function_name(**parameters_dict))

