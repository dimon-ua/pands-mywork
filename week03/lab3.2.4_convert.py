amount_of_deposit = float(input("Please enter a deposit amount:"))
converted_number = (abs(amount_of_deposit)*100)

# getting a number for an integer value
converted_number_to_int = int(converted_number)

print('That amount in cent is: {}'.format(converted_number_to_int))