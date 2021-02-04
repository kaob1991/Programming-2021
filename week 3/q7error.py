# program to fix error message on Question 7 
# author Katie O'Brien #

# message = ('I have eaten ' + 99 + 'burritos')

# error message stating it cannot concatentate int (99) with string 
# This can be fixed by adding the str type to (99)
# corrected version is below 

message = ('I have eaten ' + str(99) + ' burritos. ')

print (message)