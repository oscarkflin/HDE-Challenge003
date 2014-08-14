# HDE Challenge 003 coded in python
# Author: Oscar Lin
# Email: oscarkflin@gmail.com
# Date: 8/14/2014, USA
# Usage: Use Python.exe to open the file
# 		 and enter the input pattern that was described in HDE Challenge 003
#        Output will be printed out a line after the input.
#		 This program is used to find the sum of squares of some integers,
#    	 except negative integers.
# Note: This code is done without any kind of loop, only conditional,
#       recursion, and basic operations of variables is used.
#		This program does not catch any exception, so if the user inputted
#		anything other how it was described in HDE Challenge 003,
#		an error trace will occur and the program will end.


# Import sys.stdin
from sys import stdin

globalList = list()  # A global scope list for storing the final answer

# A method that will read the input, understand the input
# and then tokenize one of the line in order to operate 
# the necessary operation
def superSecretFormula(operation):

	# To recognize how many times the operation will be performed
	if(int(operation)>0):
		result = 0     				# The final sum
		digit = stdin.readline()	# The count of numbers that will be used
		tmp = stdin.readline()		# Temporary storage of the string
		line = tmp.split()			# List of numbers that will be used

		superSecretFormula2(int(digit), line, result)   # Perform the addition 
														# of the squared list of numbers
		superSecretFormula(int(operation)-1)			# Recursion if there's more

	# Once all the operation has performed, print the list to stdout
	else:
		print("")
		printList(globalList, 0)



# A method that will squared the numbers, and the 
# calculate the sum of all the squared number
# and will append the sum to the globalList
def superSecretFormula2(digit, line, result):
	# To see how many numbers exists
	if(digit > 0):
		#Start adding the numbers after squaring them
		if(int(line[digit-1]) > 0):
			result += square(int(line[digit-1]))
		#Recursion to add the remaining numbers
		superSecretFormula2(int(digit-1), line, result)  
	# Once this list of numbers is added, append the sum to globalList 
	else:
		globalList.append(result)

# A method that returns the square of the parameter
def square(num):
	return num*num

# A method that prints out all the content in the list
# recursively, and line by line
def printList(l, num):
	if(num < len(l)):
		print(l[num])
		printList(l, num+1)


n = stdin.readline()   # Read input to see how many operation is required
superSecretFormula(n)  # Start the operations

