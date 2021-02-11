# This program reads in numbers into the user enters 0 
# Then it will print them back out again and 
# also provide their average 

#Author Katie O'Brien 

numbers = []

#The first number we check if it is 0 in the while loop 
number = int(input ("enter a number (0 to quit): "))

while number != 0:
    numbers.append(number)

    number = int (input("enter another (0 to quit): "))

for value in numbers:
    print (value)

average = float(sum(numbers))/ len(numbers)
print ("The average is {}".format (average))