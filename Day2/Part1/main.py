def getInput(filename):
    file = open(filename)
    input = file.readlines()

    input = input[0].split(",")
    input = [i.strip() for i in input]
    
    return input

def processInput(input):
    sum = 0
    for e in input:
        #print(e)
        first = int(e.split("-")[0])
        last = int(e.split("-")[1])
        for num in range(first, last+1):
            if len(str(num)) % 2 == 0 and num // pow(10,len(str(num))/2) == num % pow(10,len(str(num))/2):
                print(num)
                sum += num
    print("RESULT: " + str(sum))

def getData(input):
    ...


def getResult(data):
    ...


input = getInput("Repos/Day2/Part1/input.txt")

processInput(input)


