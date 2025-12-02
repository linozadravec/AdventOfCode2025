def getInput(filename):
    file = open(filename)
    input = file.readlines()

    input = input[0].split(",")
    input = [i.strip() for i in input]
    
    return input

def processInput(input):
    sum = 0
    for e in input:
        first = int(e.split("-")[0])
        last = int(e.split("-")[1])
        for num in range(first, last+1):
            for length in range(1, int((len(str(num))/2)+1)):
                if len(str(num)) % length == 0:
                    part_str = str(num)[:length]
                    if part_str * int((len(str(num)) / length)) == str(num):
                        print(num)
                        sum += num
                        break

                
    print("RESULT: " + str(sum))

def getData(input):
    ...


def getResult(data):
    ...




input = getInput("Repos/Day2/Part2/input.txt")

processInput(input)


