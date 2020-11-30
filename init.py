import pandas as pd
data = pd.read_excel(r'/Users/zgrgrcn/Desktop/fuldenOdev/ilmesafe.xlsx')
ilListesi = pd.DataFrame(data, columns= ['İL ADI'])
print (ilListesi)



# distanceBetweenStates = findDistance(currentState,destinationState)