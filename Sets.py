#Sets



includes a data type for sets. 
Curly braces or the set() function can be used to create sets. 

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)	# show that duplicates have been removed 

'orange' in basket 					# fast membership testing 
'crabgrass' in basket 


Demonstrate set operations on unique letters from two words 

a = set('abracadabra')
b = set('alacazam')
a 									# unique letters in a
a - b 								# letters in a but not in b 
a | b 								# letters in a or b or both 
a & b 								# letters in both a and b 
a ^ b 								# letters in a or b but not both 

a = {x for x in 'abracadabra' if x not in 'abc'}
a


x = set('23802348')
y = set('57839012')
x - y
y - x 
x ^ y 
y | x
x & y 
x


>>>Dictionaries

#Dictionaries

#Another useful data type built into Python is the dictionary 

tel = {'jack': 4098, 'sape': 4139}
tel['sape']
tel['guido'] = 4127
tel


del tel['sape']
tel['irv'] = 4137
tel 

list(tel) #Change to List 

sorted(student) #Alphabet Sorting 

'MgOo' in student 

'MaMa' not in student 




dict([('sape',4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)

{x: x**2 for x in (2, 4, 6)}

for x in 2,4,6: 
	print(x: x**2)

2 : 4
4 : 16 
6 : 36 

>>> for x in 2,4,6: 
...     print(x,x**2)
... 
(2, 4)
(4, 16)
(6, 36)
>>> for x in 2,4,6: 
...     print(x,':',x**2)
... 
(2, ':', 4)
(4, ':', 16)
(6, ':', 36)

{x: x**5 for x in (10, 20, 30, 50)}

1 : 1
2 : 8 
3 : 27 
4 : 64 
5 : 125 



When looping through dictionaries 

knights = {'gallahad': 'the pure', 'robin': 'the brave', 'sape': 4355}
for k, v in knights.items():
	print(k, v)
('gallahad', 'the pure')
('sape', 4355)
('robin', 'the brave')

for x, y in enumerate(['tic', 'tac', 'toe']):
...     print(x,y)
... 
(0, 'tic')
(1, 'tac')
(2, 'toe')