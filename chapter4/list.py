my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]


my_string = "hello"
new_string = my_string.upper()
print(my_string)   # Output: "hello"
print(new_string)  # Output: "HELLO"

# Lists are mutable: Methods that modify a list change the original list without creating a new one.
# Strings are immutable: Methods that seem to modify a string actually return a new string, leaving the original string unchanged.