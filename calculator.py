# This part of the code defines a function
def multiply(a,b):
	return a * b

def add(a,b):
	return a + b

def substract(a,b):
	return a-b

def divide(a,b):
	return a/b

def square(a):
	return a**2

def cube(a):
	return a**3

def square_n_times(a,b):
	return a**(2*b)


# This part of the code uses the multiply function
print "I'm going to use the calculator functions to multiply 5 and 6"
x = multiply(5,6)
print x

# This part of the code uses the add function
print "I'm going to use the calculator functions to multiply 5 and 6"
x = add(5,6)
print x

# This part of the code uses the substract function
print "I'm going to use the calculator functions to substract 6 from 5"
x = substract(5,6)
print x

# This part of the code uses the divide function
print "I'm going to use the calculator functions to divide 5 by 6"
x = divide(5,6)
print x

# This part of the code uses the square function
print "I'm going to use the calculator functions to square 5"
x = square(5)
print x

# This part of the code uses the cube function
print "I'm going to use the calculator functions to cube 5"
x = cube(5)
print x

# This part of the code uses the square_n_times function
print "I'm going to use the calculator functions to square 5 6 times"
x = square_n_times(5,6)
print x