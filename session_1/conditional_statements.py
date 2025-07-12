# check = True
check = "" # "", 0, False, None

if check:
    print("evaluation success")
else:
    print("evaluation failed")


a = "aa"
b = "aa"
c = "bb"
print((a == b, b==c, a<c))
print(any((a == b, b==c, a<c)))
print(all((a == b, b==c, a<c)))

a = 1

if all([type(a) == str, type(a) == int]):
    print("it is an integer or a string")
else:
    print("other datatype")


# Todo 2 => Create an if..elif..else conditional statement to check week days. If Monday, return 1