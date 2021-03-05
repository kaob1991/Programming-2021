# Saving a data structure using the JSON module 

# Author: Katie O'Brien 


import json

filename = "testdict.json"

sample = dict(name = "Katie", age = 30, grades = [1, 34, 55])

def writeDict (obj):
    with open (filename, "wt") as f:
        json.dump(obj,f)

writeDict (sample)