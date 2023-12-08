squares = [] #making list
for value in range(1,11): 
    square = value**2 #square number for every number in range
    squares.append(square) #lines 3 and 4 can be written: squares.append(value**2)

print(squares)

#list comprehensions 
#squares = [value**2 for value in range(1,11)]
#print(squares)