import sys
import json

#get the command line argument for what
#file to run in the program
n = sys.argv

#open and load the file
f = open(n[1],)
data = json.load(f)

#create variables for each item in the input dictionary
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

#add the new transitions to the start of the
#transition table
temp2 = {"q'":newStart}
temp2.update(trans)

#set new state to be q' and insert new accepting q'
#to start of accepting states list
start = 'q\''
accept.insert(0, 'q\'')

#Print out all elements of final NFA star
print("Set of states: ", statesSet)
print("Alphabet: ", alpha)
print("Transitions: ", temp2)
print("State state: ", start)
print("Accepting states", accept)


