import sys
import pandas as pd
import numpy as np

### Database of attributes per specie

df = pd.DataFrame([
    ['Heads',1,1,1,1,1],
    ['Legs',4,2,4,4,4], 
    ['Eyes',2,2,2,2,4], 
    ['Horns',0,0,2,0,4], 
    ['Wings',0,2,0,2,2]
], columns=['things','Rabbits','Chickens','Cows','Pegasi','Demons']).set_index('things')
#print(df, file=sys.stderr)

### List of species

n = int(input())
species = input().split()
#print(species, file=sys.stderr)

### List of attributes

dico = {}
for i in range(n):
    inputs = input().split()
    thing = inputs[0]
    number = int(inputs[1])
    dico[thing] = number
#print(dico, file=sys.stderr)

### Retain possible species and their attributes

df = df[[c for c in list(df) if c in species]]
df = df.drop(index=[r for r in list(df.index) if r not in list(dico)])
#print(df, file=sys.stderr)
possible = np.matrix(df.values)
#print(possible, file=sys.stderr)

### Vector of total number of attribute

vect = [dico.get("Heads", 0), dico.get("Legs", 0), dico.get("Eyes", 0), dico.get("Horns", 0), dico.get("Wings", 0)]
#print(vect, file=sys.stderr)
vect_red = np.matrix([v for v in vect if v != 0])
#print(vect_red, file=sys.stderr)

### Solve equation system

result = np.linalg.inv(possible)*(vect_red.T)
result = [int(result.item(i)) for i in range(result.shape[0])]
#print(result, file=sys.stderr)

### Print solutions in same order than species

dic_res = {}
for i in range(len(list(df))):
    dic_res[list(df)[i]] = result[i]
#print(dic_res,file=sys.stderr)

for specie in species:
    print("{} {}".format(specie,dic_res[specie]))
