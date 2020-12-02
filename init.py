import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel(r'ilmesafe.xlsx')
df = pd.DataFrame(data)

dA=[] #distanceArray
cA=[] #citiesArray
for columnIndex in range(81):
    dA.append([])
    column=df[df.columns[columnIndex+2]]
    cA.append(column.name)
    for rowIndex in range(81):
        dA[columnIndex].append(column[rowIndex])
        # print (column[rowIndex+1])

# print(dA)
def getCityName(cityIndex):
    # return df[df.columns[1]][cityIndex-1]
    return cA[cityIndex-1]


def getCityNames(cityList):
    cityName=[] 
    for city in cityList:
        if city == 82:
            pass
        else:
            cityName.append(getCityName(city))
    return cityName


def getDistance(city1Index, city2Index):
    if city1Index >= 1 and city1Index <= 82 and city2Index >= 1 and city2Index <= 82:
        # print(getCityName(city1Index) +' to '+getCityName(city2Index))
        # return df[df.columns[city1Index+1]][city2Index-1]
        return dA[city1Index-1][city2Index-1]
    else:
        print('one of the cities is out of range (1-81)')
        return -999999


def getTotalDistance(cities):
    totalDis = 0
    index = 1
    for first, second in zip(cities[:-1], cities[1:]):
        totalDis += getDistance(first, second)
        # print(totalDis)
        # print(index)
        index = index+1
    totalDis += getDistance(cities[len(cities)-1],cities[0])    
    return totalDis

# Simulated annealing algorithm
cityList = [x for x in range(82)] 
cityList = cityList[1:]
# cityList[1] , cityList[35] = cityList[35] , cityList[1]
# print(getCityName(cityList[1]))
# print(getCityName(cityList[35]))

cost0 = getTotalDistance(cityList)
print('total distance for Turkey : ', cost0)


T = 140
factor = 0.9757
T_init = T
for i in range(100):
    print(i, 'cost=', cost0, ' T=', T)

    T = T*factor
    for j in range(10000):
        r1, r2 = np.random.randint(0,len(cityList),2)
        # print(r1,r2)
        cityList[r1], cityList[r2]=cityList[r2],cityList[r1]
        newCost=getTotalDistance(cityList)
        if newCost<cost0:
            cost0=newCost
        else:
            x = np.random.uniform()
            # 1/(1+np.exp((cost0-newCost)/T)):
            if x < np.exp((cost0-newCost)/T):
                cost0 = newCost
            else:
                cityList[r1], cityList[r2]=cityList[r2],cityList[r1]   
            
print(cost0)   
print(cityList)
print(getCityNames(cityList))