def getInput(filename):
    file = open(filename)
    input = file.readlines()
    input = [i.strip() for i in input]
    return input

def processInput(input):
    sum = 0
    for line in input:
        max_i = 0
        for i in range(1,len(line)-1):
            if line[max_i] < line[i]:
                max_i = i

        max_j = max_i + 1
        for j in range(max_j, len(line)):
            if line[max_j] < line[j]: 
                max_j = j
        sum += int(str(line[max_i]) + str(line[max_j]))
    print(sum)


def getData(input):
    ...


def getResult(data):
    ...


input = getInput("Repos/Day3/Part1/input.txt")

processInput(input)



#data = getData(input)
#result = getResult(data)
#print(input)
#resultFile = open("result.txt", "w")
#resultFile.write(str(result))


