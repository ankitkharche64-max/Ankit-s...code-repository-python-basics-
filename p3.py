#Write a python program to print the contents of a directory using the os module. 
#Search online for the function which does that. 
import os

# Specify the directory you want to list
directory_path = "/"

try:
    # Get the list of files & directories
    contents = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to access '{directory_path}'.")
