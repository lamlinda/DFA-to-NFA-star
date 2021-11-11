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
trans[accept[0]] = {}
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
print("Wrote new NFA to nowStarred.json")

#write to file
f = open("nowStarred.json", "w")

#Write opening bracket to json file
f.write("{ \n")

#write set of states to output json file
statesString = " \"setOfStates\": " + json.dumps(statesSet) + ", \n"
f.write(statesString)

#write alphabet to output json file
letters = "\"alphabet\": " + json.dumps(alpha) + ", \n"
f.write(letters)

#write transitions to output json file
transString = "\"transitions\": " + json.dumps(temp2) + ", \n"
f.write(transString)

#write start state to output json file
startString = "\"startState\": \"" + start + "\", \n"
f.write(startString)

#write accepting state to output json file
acceptString = "\"acceptingState\": " + json.dumps(accept) + "\n"
f.write(acceptString)

#write closing bracket to json file
f.write("}")





