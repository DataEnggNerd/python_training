# exception handling

input_number = 10
# addition
input_number = input_number + 23
print(input_number)
# subtract 
input_number = input_number - 10
print(input_number)
# divide
try:
    reminder = input_number / 0
except ZeroDivisionError as e:
    print(e)
    reminder = input_number 
print(reminder)
# multiply
input_number = reminder * 5
print(input_number)

# test driven development - TDD

# TODO3 => Write code which will emit NoneTypeError and AttributeError and KeyError exceptions and handle it
