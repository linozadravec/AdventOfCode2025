def getInput(filename):
    ...


def getData(input):
    ...


def getResult(data):
    ...





input = getInput("input.txt")
data = getData(input)
result = getResult(data)
print(result)
resultFile = open("result.txt", "w")
resultFile.write(str(result))