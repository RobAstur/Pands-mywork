import random 


queue = []
max_pick = 10
total_numbers = 100

for i in range (0,10):
    queue.append(random.randint(0, total_numbers))
print (f"queue is {queue}")
while len(queue) !=0:
    currentnumber = queue.pop(0)
    print(f"current number is {currentnumber} and the queue is {queue}")

print("the queue is now empty")

