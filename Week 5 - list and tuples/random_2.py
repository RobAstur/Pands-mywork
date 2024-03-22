import random

months = [ "january", "february","march","April", "may","june","july","aug","sep","oct","nov", "dic"]

for i in months:
    months.remove(random.randint(0,10))
    print(i)