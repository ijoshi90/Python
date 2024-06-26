class globalVariables:
    a = 1
    b = 2
    c = 3

# Access the variables
#print(globalVariables.a)  # Prints 1
#print(globalVariables.b)
#print(globalVariables.c)

def printVariables():
    print(globalVariables.a)
    globalVariables.b = "Overwriting b to 4"

def print2():
    print(globalVariables.b)

printVariables()
print2()
