#Reading in from a .json file 

import json
filename = "testdict.json"

def readDict():
    with open (filename) as f:
        return json.load(f)

somedict = readDict()
print (somedict)