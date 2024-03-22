car ={
"make" : "ford",
"model" : "mondeo",
"price" : 10000,
"tags" : {
    "pre-owned" : "Andrew",
    "best buy" : "dealer"}
}
#print(car)
#for key in car:
   # print(key)
   # print(key, 'has value', car[key])

for key, value in car.items():
    print(key, 'has value', value)