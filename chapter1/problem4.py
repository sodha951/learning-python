#Problem4 : Write a python program to print the contents of a directory using the os module.Search online function for the function does that.

import os

# Select the directory whose content you want to list
directory_path = 'C://trash'

# Use the os module to list the directory content
contents = os.listdir(directory_path)

for item in contents:
    print(item)