def getInput(filename):
    file = open(filename)
    input = file.readlines()
    input = [i.strip() for i in input]
    return input

def processInput(calc, input):
    resultFile = open("Repos/Day1/Part2/result.txt", "w")
    for e in input:
        print(e)
        if e.startswith("L"):
            #print(int( e.lstrip("L")))
            calc.reduce(int(e.lstrip("L")))
            #print(calc.getDial())
        if e.startswith("R"):
            #print(int( e.lstrip("R")))
            calc.increase( int(e.lstrip("R")))
            #print(calc.getDial())

        
        #if calc.getDial() == 0:
            #calc.increasePass(1)

        #print("Dial: " + str(calc.getDial()))
       # print("Pass: " + str(calc.getPass()))
        #print("############")

        resultFile.write(str(e) +  "  \n")
        resultFile.write("Dial: " + str(calc.getDial()) + " \n")
        resultFile.write("Pass: " + str(calc.getPass()) + " \n")
        resultFile.write("############ \n")


def getData(input):
    ...


def getResult(data):
    ...


class Counter:
    def __init__(self):
        self.dial = 50
        self.password = 0

    def getDial(self):
        return self.dial
    
    def getPass(self):
        return self.password
    
    def increasePass(self, number):
        self.password += number

    def reduce(self, number):
        self.increasePass(number//100)
        self.dial = self.dial - (number % 100)
        if self.dial < 0:
            if self.dial != -(number % 100):
                self.increasePass(1)
            self.dial = 100 + self.dial 
            
        elif self.dial == 0:
            self.increasePass(1)

    def increase(self, number):
        self.increasePass(number//100)
        self.dial = self.dial + (number % 100)
        if self.dial > 99:
            self.dial = self.dial - 100
            self.increasePass(1)


c = Counter()

input = getInput("Repos/Day1/Part2/input.txt")

processInput(c, input)

print(c.getDial())
print(c.getPass())

#print(51//100) #9 wholenum result

#data = getData(input)
#result = getResult(data)
#print(input)
#resultFile = open("result.txt", "w")
#resultFile.write(str(result))

