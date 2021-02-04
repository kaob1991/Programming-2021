# a program that reads in a string and tidies it up (normalises it)
# by removing any whitespace and converting to lowercase 
# it will also output the length of the original string 
# and the normalised one

# Author: Katie O'Brien

rawString = input('Please enter a string: ')
normalisedString = rawString.strip().lower()

lengthRawString = len(rawString)
lengthNormalisedString = len(normalisedString)

print('The length of the string normalised is: {}'.format(normalisedString))
print('We reduced the length of the string from {} to {}'.format(lengthRawString,lengthNormalisedString))