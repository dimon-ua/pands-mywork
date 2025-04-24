import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear']

index = random.randint(0, len(fruits)-1)

fruit = fruits[index]
print("A random Fruit:{}".format(fruit))