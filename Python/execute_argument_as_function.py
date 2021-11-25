# Reads the argument passed and calls the respective function
# Usage :
# python execute_argument_as_function.py functionsAB
# ---- or ----
# python execute_argument_as_function.py functionsCD
import sys

functionToBeExecuted = sys.argv[1] + "()"

def functionsAB():
    def functionA():
        print ("Function A is called")

    def functionB():
        print ("Function B is called")

    functionA()
    functionB()

def functionsCD():
    def functionC():
        print("Function C is called")

    def functionD():
        print("Function D is called")

    functionC()
    functionD()

# Takes the 1st argument provided executes it
try:
    exec (functionToBeExecuted)
except:
    print("Wrong argument provided while executing the function")
    print("Supported arguments functionsAB or functionsCD")
