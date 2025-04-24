import os.path
import sys

FILENAME = "moby-dick.txt"

# Getting list of command line arguments
arguments = sys.argv[:]

# Checking the correct file name
def check_file_name():
    if arguments[1] != "moby-dick.txt":
        print(f"Please write the correct file name with extension {FILENAME}")


# Checking correct file extension
def check_file_extension():
    if arguments[1].endswith('.txt'):
        pass
    else:
        print(f"Please type the correct file extension")  


# try catch block with checking errors
try:        
    with open(FILENAME, 'r') as f:
        data = f.read()
        count_e = data.count('e')
except FileNotFoundError: 
    # Checking if the file does exist
    if not os.path.isfile(FILENAME): 
        print(FILENAME, "file doenst exist")
except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Checking command line with correct arguments
if len(sys.argv) < 2:
    print(f"1 argument expected, please enter the name of the file: {FILENAME}")           
else:
    check_file_name()
    check_file_extension()
    print(count_e)
    
    



