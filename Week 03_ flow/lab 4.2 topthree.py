import random
list_random =[]
random_numbers = int(random.randint(1,100))
i = 0
while i <10:
    i += 1
    list_random.append(random_numbers)
    random_numbers = int(random.randint(1,100))
    list_random.sort()
print(list_random)
print(f"the highest values are, {list_random[7:10]}")

    
   

  