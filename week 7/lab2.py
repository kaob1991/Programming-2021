# Messing with files 
# Write a program that counts how many times it was run 

# Author: Katie O'Brien 

filename = "count1.txt"

def readNumber ():
    with open (filename) as f:
        number = int(f.read())
        return number

def writeNumber (number):
    with open(filename, "wt") as f:
        f.write(str(number))

num = readNumber()
num += 1 

print ("We have run this program {} times".format(num))
writeNumber(num)