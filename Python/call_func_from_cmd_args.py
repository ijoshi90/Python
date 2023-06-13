# Function to call the def from command line arguments

# Run as call_func_from_cmd_args.py functionA "Parameter 1"
import sys

def functionA(param1):
    print("Function A Called")
    print(param1)

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
