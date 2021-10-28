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
    elif i == "transitions":
        trans = data[i]
    elif i == "startState":
        start = data[i]
    elif i == "acceptingState":
        accept = data[i]

#print(statesSet)
#print(statesSet[0])

#print(trans)
print(trans['q0']['b'])


