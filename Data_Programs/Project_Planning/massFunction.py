import library

data = library.loadList('exoplanet.csv')

#PlanetIdentifier,TypeFlag,PlanetaryMassJpt,RadiusJpt,PeriodDays,SemiMajorAxisAU,Eccentricity,PeriastronDeg,LongitudeDeg,AscendingNodeDeg,InclinationDeg,SurfaceTempK,AgeGyr,DiscoveryMethod,DiscoveryYear,LastUpdated,RightAscension,Declination,DistFromSunParsec,HostStarMassSlrMass,HostStarRadiusSlrRad,HostStarMetallicity,HostStarTempK,HostStarAgeGyr
col = {'name':0,'massJpt':2,'radiusJpt':3,'periodDays':4,'smaAU':5,'ecc':6,'tempK':11,'ageB':12,'method':13,'year':14,'RA':16,'D':17,'stMassSolar':19,'stRadSolar':20,'stMt':21,'stTempK':22,'stAgeB':23}

print("MASSES OF PLANETS:")

#setting counters:
large = 0
small = 0
unknown = 0

for n in range(0,len(data)):
    #in the case the we know the mass:
    if data[n][col['massJpt']] != '': 
        #if the mass is larger than or smaller than jupiter's (CSV is in jupiter masses):
        if float(data[n][col['massJpt']]) > 1:
            large += 1
        elif float(data[n][col['massJpt']]) <= 1:
            small += 1

#calculating the percent from total (all planets with known masses), and printing:
total = large + small
larger = large / total * 100
print(str(round(larger,1)) + "% of planets with a known mass have a larger mass then jupiter.")

smaller = small / total * 100
print(str(round(smaller,1)) + "% of planets with a known mass have a smaller mass then jupiter.")
