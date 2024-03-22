FILENAME = "data.txt"
'''
with open(FILENAME, 'r') as f:
    data = f.read()
    print(data)

with open(FILENAME, 'r') as f:
    for data in f:
        print(data.strip())
'''

with open("data2.txt", "w+") as f:
    f.write ("how now\n")
    f.write ("brown cow")
    f.seek(0)
    data = f.read()
    print(data)

print("done")