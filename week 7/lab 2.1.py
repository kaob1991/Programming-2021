# Creating the count.txt file 
# As part of the lab 2 work 

# Author Katie O'Brien 



import os.path
filename = "count.txt"

if not os.path.isfile(filename):
    print ("file does not exist")

def readNumber ():
    try: 
        with open ("count.txt") as f:
            number = int (f.read())  
            return number 

    except IOError:
        return 0