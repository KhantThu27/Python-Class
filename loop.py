#Loops

loop.py

-While Loops
-for Loopss

Condition is true, while loop execute a set of statements

x = 1
while x < 7:
	print(x)
	x += 1



While loop require variable ready/

x = 1
while x < 7:
	print(x)
	if x == 5:
		break
	x += 1


==================================================

For Loops 

#for loops is iterating over a sequence

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	print(x)

#looping in a String

for x in "pineapple":
	print(x)

#The break Statement

# stop after condition

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	print(x)
	if x == "pineapple":
		break

----
#stop before condition

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	if x == "pineapple":
		break
		print(x)


#The continue statement - stop the current iteration 

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	if x == "pineapple":
		continue
		print(x)


#The range() function - a set of code a specified number 

for x in range(10):
	print(x)


for x in range(10,100):
	print(x)


for x in range(10,100,5):
	print(x)


#Nested Loops

NumberA = [1, 2, 3, 4, 5]
NumberB = [1, 2, 3, 4, 5]
NumberC = [1, 2, 3, 4, 5]

for x in NumberA:
	for y in NumberB:
		for z in NumberC:
			print(x,y,z)
		

#Pass 

for x in [1, 2, 3, 4, 5]: