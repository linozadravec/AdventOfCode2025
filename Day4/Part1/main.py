def getInput(filename):
    file = open(filename)
    input = file.readlines()
    input = [i.strip() for i in input]
    return input

def processInput(input):
    sum = 0
    rows = len(input)
    columns = len(input[0])
    # arr_adjecency = [[0] * columns] * rows # WRONG, references same object
    arr_adjecency = [[0 for x in range(columns)] for y in range(rows)] 
    

    # arr_adjecency[1][1] = 1

    for r in range(0,rows):
        lin = ""
        for c in range(0, columns):
            lin += str(arr_adjecency[r][c]) + " "
        print(lin)
    
    arr_nearby  = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]

    for idx_line, line in enumerate(input):
        for idx_char, char in enumerate(line):
            #print(str(idx_line) + " " + str(idx_char))
            if char == "@":
                #print("FOUND @ on (" + str(idx_line) + ", " + str(idx_char) + ")")
                for nearby in arr_nearby:
                    if 0 <= idx_line + nearby[0] < rows and  0 <= idx_char + nearby[1] < columns:
                        #print(str(idx_line + nearby[0]) + " " + str(idx_char + nearby[1]))
                        # print()
                        arr_adjecency[idx_line + nearby[0]][idx_char + nearby[1]] += 1
                        # arr_adjecency[idx_char + nearby[0]][idx_line + nearby[1]] += 1

                # print(line.index)
                # print(char.index)
    for idx_line, line in enumerate(input):
        for idx_char, char in enumerate(line):
            if char == "@" and arr_adjecency[idx_line][idx_char] < 4:
                sum += 1
    # lin = 
    # for r in range(0,rows):
    #     lin = ""
    #     for c in range(0, columns):
    #         lin += str(arr_adjecency[r][c]) + " "
    #     print(lin)
    
    print(sum)


def getData(input):
    ...


def getResult(data):
    ...


input = getInput("Repos/Day4/Part1/input.txt")

processInput(input)



#data = getData(input)
#result = getResult(data)
#print(input)
#resultFile = open("result.txt", "w")
#resultFile.write(str(result))


