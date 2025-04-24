import numpy as np

min_salary = 20000
max_salary = 80000
number_of_entries = 10

np.random.seed(1) 

salaries = np.random.randint(min_salary, max_salary,number_of_entries)

print (salaries)
