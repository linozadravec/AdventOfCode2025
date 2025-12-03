def getInput(filename):
    file = open(filename)
    input = file.readlines()
    input = [i.strip() for i in input]
    return input

def processInput(input):
    sum = 0
    for line in input:
        result = ""
        # SOLUTION W/OUT max_i
        cur_max = 0
        for remaining in range(11, -1, -1):
            for i in range(cur_max, len(line) - remaining):
                if line[cur_max] < line[i]:
                    cur_max = i
            result += line[cur_max]
            cur_max += 1
        sum += int(result)
    

        # SOLUTION
        # current = 1
        # max_i = 0
        # for remaining in range(12, 0, -1):
        #     for i in range(current,len(line)-remaining + 1):
        #         if line[max_i] < line[i]:
        #             max_i = i
        #     result += line[max_i]
        #     max_i = max_i + 1
        #     current = max_i + 1
        # sum += int(result)
    print(sum)


def getData(input):
    ...


def getResult(data):
    ...


input = getInput("Repos/Day3/Part2/input.txt")

processInput(input)



#data = getData(input)
#result = getResult(data)
#print(input)
#resultFile = open("result.txt", "w")
#resultFile.write(str(result))


