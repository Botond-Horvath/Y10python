import library

data = library.loadList("exoplanet.csv")

#PlanetIdentifier,TypeFlag,PlanetaryMassJpt,RadiusJpt,PeriodDays,SemiMajorAxisAU,Eccentricity,PeriastronDeg,LongitudeDeg,AscendingNodeDeg,InclinationDeg,SurfaceTempK,AgeGyr,DiscoveryMethod,DiscoveryYear,LastUpdated,RightAscension,Declination,DistFromSunParsec,HostStarMassSlrMass,HostStarRadiusSlrRad,HostStarMetallicity,HostStarTempK,HostStarAgeGyr
col = {'name':0,'massJpt':2,'radiusJpt':3,'periodDays':4,'smaAU':5,'ecc':6,'tempK':11,'ageB':12,'method':13,'year':14,'RA':16,'D':17,'stMassSolar':19,'stRadSolar':20,'stMt':21,'stTempK':22,'stAgeB':23}

print("Here are the possible datapoints of interest: ")
print(list(col.keys()))

userInput = str(input("\nEnter a datapoint (important that you enter correctly or program will crash): \n"))

#defining counters and lists
knownCounter = 0
unknownCounter = 0
densityCounter = 0
densityList = []

#Loop counting the number of planets in dataset...
for n in range(0,len(data)):
    if data[n][col[userInput]] == '': #... with unknown input parameter
        unknownCounter += 1
    else: #... or with known input parameter
        knownCounter += 1

#Loop counting number of planets with known densities (not in csv)
for n in range(len(data)):
    #We can only calculate the density if we know the mass and the radius:
    if data[n][col['massJpt']] != '' and data[n][col['radiusJpt']] != '':
        densityCounter += 1 # if density can be calculated, adds that planet to the counter
        densityList += [data[n][col['name']]] #also adds the planet to a list

#Percentages of known, unknown, and planets with known density:
unknownPercent = unknownCounter / len(data) * 100 
knownPercent = knownCounter / len(data) * 100
densityPercent = densityCounter / len(data) * 100

#printing
print("No known data on this: " + str(round(unknownPercent,0)) + "%")

print("Known data on this: " + str(round(knownPercent,0)) + "%")

cont = str(input("Do you want to find information of density? If yes, type: yes\n"))
if cont == "yes":
    print("We know the densities of " + str(round(densityPercent,2)) + "% of the planets, these are:")
    print(densityList)
