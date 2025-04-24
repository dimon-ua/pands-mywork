import random

queue = []
index = 0

for element in range(0,100):
    while len(queue) < 10:        
        queue.append(random.randint(0,101))    

print(f"queue is {queue}")

while len(queue) !=0:
    current_element = queue.pop(0)
    print(f"current number is {current_element} and the queue is {queue}")
    
print("The queue is now empty")