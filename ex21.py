def add(a,b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a-b
	
def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b
	
def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b

def meat():	
	op = raw_input ("What operation would you like to do? ")

	if op == "addition":
		num1, num2 = raw_input("What two numbers would you like to add? \n > ").split()
		num1 = int(num1)
		num2 = int(num2)
		sum = num1 + num2
		print "%d + %d = %d" % (num1, num2, sum)
		
		
		again = raw_input("Would you like to calculate again? (Y/N)\n > ")
		if again == "Y":
			meat()
		else:
			quit()
	if op == "subtraction":
		num1, num2 = raw_input("What two numbers would you like to subtract? \n > ").split()
		num1 = int(num1)
		num2 = int(num2)
		diff = num1 - num2
		print "%d + %d = %d" % (num1, num2, diff)
		
		again = raw_input("Would you like to calculate again? (Y/N)\n > ")
		if again == "Y":
			meat()
		else:
			quit()
	if op == "multiplication":
		num1, num2 = raw_input("What two numbers would you like to multiply? \n > ").split()
		num1 = int(num1)
		num2 = int(num2)
		product = num1 + num2
		print "%d + %d = %d" % (num1, num2, product)
		
		if again == "Y":
			meat()
		else:
			quit()
	if op == "division":
		num1, num2 = raw_input("What two numbers would you like to divide? \n > ").split()
		num1 = int(num1)
		num2 = int(num2)
		quotient = num1 + num2
		print "%d + %d = %d" % (num1, num2, quotient)

		if again == "Y":
			meat()
		else:
			quit()
meat()