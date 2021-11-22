# DFA-to-NFA-star
Given a DFA or NFA, give the NFA for its'star

To run the program, type "python NFA-Star.py" followed by the json file containing the DFA/NFA you want to preform the star operation on.

Example: "python NFA-Star.py testing.json"

Included in this project are 10 test files which go from:
testing.json
testing2.json
testing3.json
.
.
.
testing9.json
testing10.json

The first 5 test files (testing.json - testing5.json) contain valid DFA/NFAs while the last 5 test files (testing6.json - testing10.json) 
have an error in the file/formal description format and demonstrates that the program will exit cleanly even on bad inputs.

To create a test file, follow the formal description format.
Example:

{
    
    setOfStates": ["q0", "q1", "q2", "q3"],
    "alphabet": ["a", "b"],
    
    "transitions": {"q0":{"a":"q1", "b":"q2"},  //our files are formatted so that in this line, at q0 on an 'a' will go to state q1 and so on
                    "q1":{"a":"q3", "b":"q1"},
                    "q5": {"a":"q2"},
                    "q2":{"a":"q2", "b":"q2"},
                    "q3":{"a":"q3", "b":"q1"}
                    },
                    
    "startState": "q0",
    "acceptingState": ["q3"]
}

Test files must be written in this format or an error message will print and the program will exit.
