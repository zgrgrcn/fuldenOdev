import pandas as pd
data = pd.read_excel(r'ilmesafe.xlsx')

df = pd.DataFrame(data)
##print (df[df.columns[1]])

for columnIndex in range(2, 83):
    column=df[df.columns[columnIndex]]
    for rowIndex in range(1, 81):
        print (column[rowIndex])

print("bitti")
# distanceBetweenStates = findDistance(currentState,destinationState)

T=30
factor =0.99
T_init=T
for i in range(1000):
    print(i, 'cost=',cost0)
    
    T=T+factor
    for j=in range(500):