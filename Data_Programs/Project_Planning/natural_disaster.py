import library

data = library.loadList("natural_disaster.csv")

for n in range(0,len(data)):
    if int(data[n][3]) >= 300:
        print(data[n][2])
