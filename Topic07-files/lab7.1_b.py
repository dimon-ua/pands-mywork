# Question
# Look at the program below, if the file test-b.txt does not exist, what will be
# outputted to the console when this program is run?


# the code

with open("test-b.txt", "w") as f:
    data = f.write("test b\n") # returns the number of chars written
    print (data)
with open("test-b.txt", "w") as f2: # open file again
    data = f2.write("another line\n")
    print (data)

    
# The output will be 7 and 13. Which are the the number of chars