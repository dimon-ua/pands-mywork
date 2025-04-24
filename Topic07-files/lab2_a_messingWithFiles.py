import os.path
import json

FILENAME="testdict.json"
sample = dict(name='fred', age=31, grades=[1,34,55])
def writeDict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)
#test the function
writeDict(sample)

FILENAME = "count.txt"

def writeNumber(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))
        

if not os.path.isfile(FILENAME):
    print ("File does not exist")
    #initialise file here
    writeNumber(0)


def readNumber():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
 # this file will be created when we write back.
 # no file assumes first time running
 # ie 0 previous runs
        return 0
    
num = readNumber()
print(num)


# writeNumber(3)

# main

num = readNumber()
num += 1
print(f"we have run this prog {num} times")

writeNumber(num)