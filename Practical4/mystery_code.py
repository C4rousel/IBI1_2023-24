# What does this piece of code do?
# Answer:Take a random number between one and ten, take it a hundred times and add it up to find the sum

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
#define the initial value
progress=0
total_random_number=0
while progress<100:#start a loop when progress is less than 100
	#with progress increases 1, the total random number increases by a random number between one and ten
	progress+=1 #Limit the times of taking the number of random numbers is one hundred
	n = randint(1,10) #Limit the range of random numbers to 1 to 10
	total_random_number = total_random_number+n # Add all random numbers to find a sum

print(total_random_number) # print the answers
