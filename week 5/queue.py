# Puts 10 random numbers in a queue 
# Outputs all the values in the queue 
# One at a time take the numbers from the queue and print, along with the other numbers still in the queue 

# Author: Katie O'Brien 

import random 

queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range (0, numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print("queue is {}".format(queue))

while len(queue) != 0:

    currentNumber = queue.pop (0)
    print ("current Number is {} and the queue is {}".format(currentNumber, queue))

print ('The queue is now empty')

