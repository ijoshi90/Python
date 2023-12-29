from time import time
from random import *
from time import sleep

uniqueID = ""
def randomNumber():
    return (randrange(5, 25))
def generateUniqueID():
    global uniqueID
    uniqueID = "uid_" + str(int(time()))
def B():
    print("In Def B")
    sleep(randomNumber())
def A():
    print("In Def A")
    sleep(randomNumber())
    B()

# Main
if __name__ == '__main__':
    generateUniqueID()
    print("Unique ID at Beginning : {}, insert data to influx".format(uniqueID))
    A()
    print("Unique ID at End : {}, insert data to influx".format(uniqueID))

