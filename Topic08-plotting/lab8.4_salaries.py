import numpy as np

min_salary = 20000
max_salary = 80000
number_of_entries = 10

np.random.seed(1) 

salaries = np.random.randint(min_salary, max_salary,number_of_entries)

salaries_plus = salaries + 5000 

salaries_multiply = salaries * 1.05

new_salaries = salaries_multiply.astype(int)
print(new_salaries)