print("Enter first number")
try:
	firstNum = input()
	print("You have Entered {firstNum}")
	print("Enter second number")
	secondNum = input()
	print("You have Entered {secondNum}")
	print("Select Operations")
	print("""1. Addition 
		 2. Subtraction
		 3. Multiplication
		 4. Division
		 5. Modulus""")
	userInput = input()
except exception:
	print("Wrong input might be reason")
if userInput == 1:
	print("You have selected Addition")
	total = firstNum + secondNum
	print("Total : {total}")
