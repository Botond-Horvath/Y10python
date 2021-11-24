import library
from matplotlib import pyplot as plt

data = library.loadList('exoplanet.csv')

#PlanetIdentifier,TypeFlag,PlanetaryMassJpt,RadiusJpt,PeriodDays,SemiMajorAxisAU,Eccentricity,PeriastronDeg,LongitudeDeg,AscendingNodeDeg,InclinationDeg,SurfaceTempK,AgeGyr,DiscoveryMethod,DiscoveryYear,LastUpdated,RightAscension,Declination,DistFromSunParsec,HostStarMassSlrMass,HostStarRadiusSlrRad,HostStarMetallicity,HostStarTempK,HostStarAgeGyr
col = {'name':0,'massJpt':2,'radiusJpt':3,'periodDays':4,'smaAU':5,'ecc':6,'tempK':11,'ageB':12,'method':13,'year':14,'RA':16,'D':17,'stMassSolar':19,'stRadSolar':20,'stMt':21,'stTempK':22,'stAgeB':23}

mtList = []
ageList = []

for n in range (len(data)):
    #if we know the metallicity and the age of a star (2 parameters compared):
    if data[n][col['stMt']] != '' and data[n][col['stAgeB']] != '':
        mtList.append(float(data[n][col['stMt']])) #adds the metallicity to its list
        ageList.append(float(data[n][col['stAgeB']])) #adds the age to its list

print('Here are the metallicity-age pairs for the stars that we know them for: ')
#the lengths of the 2 lists are equal, so it doesn't matter which I use:
for n in range(len(mtList)):
    #prints that metallicity/age pairs for all planets where this is known
    print(str(mtList[n]) + ' ; ' + str(ageList[n])) 

#A little extra printing what the maximum and minimum MTs are, to get an idea of the range:
print("The maximum metallicity is: " + str(max(mtList)) + ", and the minimum is: " + str(min(mtList)))


#Using matplotlib in order to scatter these pairs as coordinates:
plt.title('Star Metallicity vs. Temperature')
plt.xlabel('Age (Ga)')
plt.ylabel('Metallicity')

plt.scatter(ageList,mtList,s=10) #(x,y,size)
plt.show()