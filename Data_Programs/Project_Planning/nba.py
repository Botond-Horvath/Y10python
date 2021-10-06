import library

# top: ,name,gp,min,pts,fgm,fga,fg,3p_made,3pa,3p,ftm,fta,ft,oreb,dreb,reb,ast,stl,blk,tov,target_5yrs
data = library.loadList("nba.csv")

col = {"name":1,"fgm":5,"fga":6}

print("These are the players with field goals of more than 3:")

counter = 0
total = 0
for n in range(0,len(data)):
    if float(data[n][col['fgm']]) >= 3:
        print(data[n][col['name']])
        print(data[n][col['fgm']])
        total += float(data[n][col['fgm']])
        counter += 1

print("The number of players with field goals above 3 is: ", counter)

average = total / counter
roundedAverage = round(average,2)
print("The average of field goals above 3 is: " + str(roundedAverage))