import pandas as pd

listDAta= [
    ['John', 'math', 23],
    ['John', 'programming', 66],
    ['Mary', 'math', 45],
    ['Mary', 'programming', 33],
    ['Mark', 'SIEM', 57],
    ['Mark', 'programming', 70],
    ['Mark', 'math', 73],
    ['John', 'programming', 61]
]
df = pd.DataFrame(listDAta, columns=['name','subject','grade'])
print(df.head(3))
print(df.describe())
print(type(df.describe()))

path = "./data/"
csv_file_name = path + 'grades.csv'
df.to_csv(csv_file_name)

# CSV file will start with comma, because CSV file uses a comma as a delimeter

excel_file_name = path +'grades.xlsx'
df.to_excel(excel_file_name, index=False, sheet_name='data')

with pd.ExcelWriter(excel_file_name, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name="summary")
    
mean = df.describe().loc['mean','grade']
print(mean)

# mean = df['grade'].mean()
# print (mean)