#Even or odd numebrs exercise
#An even number is an integer that can be divided by two and remain an integer or has no remainder. For example, is an even number, because =, and is an integer. Definition. If an even number is divided by two, the result is another integer.
#Odd numbers are positive integers that cannot be divided into two equal parts.

Type_number = int(input("Add one number"))
if Type_number % 2 ==  0:
    print("you have selected: ",Type_number)
    print(Type_number, "// by 2 is an even number")
else:
    print( "is and odd numebr")