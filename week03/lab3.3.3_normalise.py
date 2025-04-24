raw_string = input("please enter a string: ")
normal_string = raw_string.strip().lower()

raw_string_len = len(raw_string)
normal_string_len = len(normal_string)

print("That string normalised is: {}".format(normal_string))
print("We reduced the input string from {} to {}".format(raw_string_len, normal_string_len))