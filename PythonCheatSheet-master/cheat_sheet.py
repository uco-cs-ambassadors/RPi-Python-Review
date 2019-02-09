#Review and Cheat Sheet

#Comments
# This comment is on its own line
print("I could have comments like this: \n")  # This comment is on the same line as the code


#Print
print('I can use single quotes')
print("I can use double quotes")
print('Double "quotes" within single "quotes" will print the quotation marks\n')

#Variables
name = "Ben"
age = 25
print("My name is", name + '. I am', age, "years old.\n")


#Functions
def print_info(name, age):
	print("Name:", name, "\t Age:", age)

print_info("Caesar", 20)
print_info("Lucca", 17) 

#For-In Loop
print("") 
for i in range(5):
	print(i)

print("")

# This function demonstrates the if-then-else statements
def play_game():
	my_age = int(input("How old are you? "))
	if (my_age > 120):
		print("You must be a vampire")
	elif (my_age > 17):
		print("You are an adult")
	elif (my_age > 12):
		print("You are a teenager")
	elif (my_age > 4):
		print("You are a child")
	elif (my_age > 0):
		print("You are a toddler")
	elif (my_age > -1):
		print("You are a baby")
	else:
		print("That’s impossible!")

# This function demonstrates acquiring user input
def ask_question():
	global cmd   # By identifying this variable as global, it can be used outside of the function that created it
	cmd = input("Do you want to play? (y/n) ")

# Calling a function
ask_question()

# Demonstrates while loop
if cmd == 'y':
	while cmd == 'y':
		play_game()
		ask_question()

