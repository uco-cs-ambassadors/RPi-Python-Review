# PythonCheatSheet

Review and Cheat Sheet

Download the code example from: https://github.com/GinaQ/PythonCheatSheet.git

# Shutting Down the Raspberry Pi:
Go to the menu at the top of the left corner.
Scroll all the way down and double click on shut down.
It will ask you for confirmation. Click on “Shut down”.

# Comments are used to tell what something does. 
They are very important to your program. A comment is identified with the ‘#’ sign.<br> 
Examples: 

    # This comment is above the code
    print(“I could have comments like this: \n“)  # This comment is on the same line as the code
Console:

    I could have comments like this: 

# Print a message on the console.<br>
Examples:

    print(‘I can use single quotes’)
    print(“I can use double quotes”)
    print(‘Double “quotes” within single “quotes” will print the quotation marks\n’)
Console: 

    I can use single quotes
    I can use double quotes
    Double “quotes” within single “quotes” will print the quotation marks

# Variables can make your program easier to understand and to write. <br>
Examples:

    name = “Ben”
    age = 25

Both commas [,] and plus sign [+] will join two parts together. <br>
Comma adds a space. Plus sign does not add a space.

    print(“My name is“, name + “. I am“, age, “years old.\n”)
                      ↑      ↑         ↑    ↑
                    space  no space  space space
Console:

    My name is Ben. I am 25 years old.
              ↑   ↑     ↑  ↑
            space x   space space

# Functions can also make your program easier to understand and write. 
Functions do three things: <br>
They name pieces of code the way variables name strings and numbers. <br>
They can accept ‘arguments’. Arguments are simply data or variables that are passed into the function <br>
They can be called numerous times by using the function name (and arguments, if any) <br>

You can create your own functions… <br>

Examples:

    def print_info(name, age):
        print("Name:", name, "\t Age:", age)

    print_info(“Caesar”, 20)
    print_info(“Lucca”, 17) 
                  ↑       ↑
                  arguments

Console: 

    Name: Caesar     Age: 20
    Name: Lucca      Age: 17

Or utilize predefined functions… 

# Libraries are a collection of predefined functions. 
Some libraries are inherently available, others must be imported. <br>
Examples: 

    # There is no need to import a library for the print function:
    print(“some message”) 

    # You must import time to use the sleep() function
    import time
    time.sleep(1)

# Loops are functions that repeat (iterate) based on a certain condition.

Example (for...in range(...) loop):

    # Loop iterates through the range
    for i in range(5):
        print(i)

Console:

    ## variable ‘i' begins at zero and runs through the loop 5 times
    0
    1
    2
    3
    4

Example (while loop)

    while True:
        print(“I am the program and I am running”)
        time.sleep(2)

Console:

    In this example, the while loop will print a message every two seconds  until the program is terminated.
        

# If-Then statements specify an action to perform if a specific condition exists. 
Although “then” is not actually typed, it is assumed for all code that is indented under the if statement. Else and else-if (elif) can be used to add additional conditions and actions. <br>

Example: 

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

Console: 

    How old are you? 3
    You are a toddler



