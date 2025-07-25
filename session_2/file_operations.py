file_name = "agenda.txt" # add absolute path

# open the file 
# read the content of the file and print
# add one line to the file

# file modes => r - read; a - append; w - write

file_obj = open(file_name, mode="r")
file_content = file_obj.read()
file_obj.close() # very important
print(file_content)

# TODO1 => difference between read(), readline() and readlines()

# context managers - reference
file_content = ""
with open(file_name, mode="r") as file_obj:
    file_content = file_obj.read()

file_obj = open(file_name, "a")
file_obj.write("\n9. test text")
file_obj.close()

# context managers - reference

with open(file_name, mode="a") as file_obj:
    file_obj.write("\n10. with context manager")

# TODO2 => difference between a mode and w mode 