import random

numbers = []

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeto = 100
numbers = []

for i in range(0,howMany):
    numbers.append(random.int(rangeFrom, rangeto))
    
print (f"{howMany} random numbers\t {numbers}")

topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {topHowMany} are \t\t {topOnes[0:topHowMany]}")
