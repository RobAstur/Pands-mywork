import  random
guess_number = random.randint(1,100)
i = 0
x = int(input("PLease guess the number from 1 to 100 "))
while x != guess_number:
    i+=1
    print(i)
    print("thats not correct")
    if i == 5:
        print("yuo have reach max attempts")
        break
    if x > guess_number:
        print("thats too high")
    else:
        print("thats too low, keep trying")
    x = int(input("PLease guess the number "))
    print("thats correct")
    
