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

#transition from q0 on b
#print(trans['q0']['b'])

#make new transition from accepting state to initial start state

#create a temporary state and make it transition from
#accepting state to start state for A*
temp = trans[accept[0]]
temp["E"] = start

#Overwrite the accepting state with the temp state
data['transitions'][accept[0]] = temp

#make new start state q'
statesSet.insert(0, 'q\'')

#Make transition from q' to initial start state
trans['q\''] = {} 
newStart = trans['q\'']
newStart["E"] = start
data['transitions']['q\''] = newStart

temp2 = {"q'":newStart}

temp2.update(trans)


#set new state to be q'
start = 'q\''

accept.insert(0, 'q\'')

print(temp2)

print(accept)


