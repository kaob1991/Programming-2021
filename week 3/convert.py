#program to convert dollars to cents and return an absolute number 
  
# Author: Katie O'Brien 

originalValue = float(input('Please enter an amount: ')) 
# This takes in a float amount, needed for dollars and cent

absoluteValue = abs(originalValue)
# This converts the amount into an absolute figure

centAmount = int(absoluteValue*100)
#This converts the amount into cents 

print('That amount in cent is: {}'.format(centAmount))