import library as lib

playerData = lib.loadList('playerInfo.csv')
countryData = lib.loadList('countryInfo.csv')

#Player:
#PlayerId,NameFirst,NameLast,CurrentHandle,CountryCode,TotalUSDPrize,Game,Genre
#Country:
#Continent_Name,Continent_Code,Country_Name,Two_Letter_Country_Code,Three_Letter_Country_Code,Country_Number

col = {'country_name':2,'country_code':3,'player_country_code':4,'total_earnings':5}

list = []
noPlayer = []
for n in range(0,len(countryData)):
    totalEarnings = 0
    playerCount = 0
    countryCode = countryData[n][col['country_code']].lower()
    for p in range(0,len(playerData)):
        if countryCode == playerData[p][col['player_country_code']]:
            totalEarnings += float(playerData[p][col['total_earnings']])
            playerCount += 1
    if playerCount > 0:
        earningAverage = totalEarnings / playerCount
        countryName = countryData[n][col['country_name']]
        list += [[countryName,playerCount,round(totalEarnings,2),round(earningAverage,2)]]
    else:
        noPlayer += [countryData[n][col['country_name']]]

for i in list:
    print(i)

print("Other than this, there are " + str(len(noPlayer)) + " countries not represented in e-sports")