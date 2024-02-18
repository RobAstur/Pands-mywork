
guess_number = "50"
x = ""
while x != guess_number:
    x = (input("please guess the number"))
    if x == guess_number:
        print("Thats correct")
    else:
        print("keep trying")