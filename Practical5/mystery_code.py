# What does this piece of code do?
# Answer:progress+1 and draws a number between 1 and 100 in every loop, at the 11th loop, pregress=10, so the loop break, print n

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0 #give progress a definiton
while progress<10: #give a limit
	progress+=1 #progress+1 at every loop
	n = randint(1,100) #draws a number between 1 and 100

print(n) #output the value of n
