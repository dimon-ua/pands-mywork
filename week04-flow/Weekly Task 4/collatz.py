positive_integer = int(input("Enter any positive integer: "))

numbers_list = []
numbers_list.append(positive_integer)
index = 0

while numbers_list[index] != 1:  # interrupt the programm to avoid infinite loop 1-4-2-1  
    if numbers_list[index] % 2 == 0:
        numbers_list.append(numbers_list[-1]//2)     
        index +=1   
    else:
        numbers_list.append(numbers_list[-1] * 3 + 1)        
        index +=1  
    
print(numbers_list)