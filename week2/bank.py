amount1 = input("Please enter first amount(in cent) ")
amount2 = input("Please enter second amount(in cent) ")
amount1 = int(amount1) / 100
amount2 = int(amount2) / 100

sum = amount1 + amount2

print(f'The sum of these is \N{euro sign}{sum}')