def years (m):
    return m * 100
metros = years(1.76)
print(metros)

     



'''
def numbers ():
    real_numbers = []
    numbers_list = int(input("add a number"))
    real_numbers.append(numbers_list)
    while numbers_list != 0:
        print("0 to quit")
        numbers_list = int(input("add a number"))
        real_numbers.append(numbers_list)
    return real_numbers

real_numbers = numbers()
print(real_numbers)
'''






'''
numbers = []
pregunta = int(input("please add a number "))
while pregunta != 0:
    numbers.append(pregunta)
    pregunta = int(input("please add a number "))
for i in numbers:
    print(i)
average = int(sum(numbers))/len(numbers)
print(average)
sum = sum(numbers)
print(sum)
'''