import sys
import json


def readFile(file):

  

    return

f = open('testing.json',)

data = json.load(f)

for i in data:
    if i == "setOfStates":
        statesSet = data[i]
    elif i == "alphabet":
        alpha = data[i]

print(statesSet)
print(statesSet[0])

