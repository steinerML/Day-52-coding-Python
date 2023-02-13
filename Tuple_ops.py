#TUPLE Operations
tuple1 = (1,'apple',3,'banana',5)

# dict1 = {'1': 'A', '2': 'B'}

# print(dict1['1'])

#Access elements in a tuple
print(tuple1[0]) #1st element
print(tuple1[1]) #2nd element
print(tuple1[2]) #3rd element
print(tuple1[3]) #4th element
print(tuple1[4]) #5th element

#Count number of elements
print(tuple1.count('apple'))
print(tuple1.count(5))
print(tuple1.count('banana'))

#INDEX, returns the index of a given element
print(tuple1.index('apple')) #Index 1
print(tuple1.index('banana')) #Index 3

#3 ways to append a tuple (even if it's unmmutable by definition)

#TUPLE unpacking
tuple1 = (*tuple1, 'Hello')
print(tuple1)

#TUPLE concatenation
tuple1 = tuple1 + ('Goodbye!',)
print(tuple1)

#List conversion
a = list(tuple1)
a.append('Ciao!')
tuple1 = tuple(a)
print(tuple1)
