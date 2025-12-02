def getInput(filename):
    file = open(filename)
    input = file.readlines()
    input = [i.strip() for i in input]
    return input

def processInput(calc, input):
    for e in input:
        if e.startswith("L"):
            #print(int( e.lstrip("L")))
            calc.reduce(int( e.lstrip("L")))
            #print(calc.getDial())
        if e.startswith("R"):
            #print(int( e.lstrip("R")))
            calc.increase( int( e.lstrip("R")))
            #print(calc.getDial())

        
        if calc.getDial() == 0:
            calc.incrementPass()

        print(calc.getDial())
        print(calc.getPass())
        print("############")


def getData(input):
    ...


def getResult(data):
    ...


class Counter:
    def __init__(self):
        self.dial = 50
        self.password = 0

    def reduce(self, number):
        self.dial = self.dial - (number % 100)
        if self.dial < 0:
            self.dial = 100 + self.dial 

    def increase(self, number):
        self.dial = self.dial + (number % 100)
        if self.dial > 99:
            self.dial = self.dial - 100

    def getDial(self):
        return self.dial
    
    def getPass(self):
        return self.password
    
    def incrementPass(self):
        self.password += 1

c = Counter()

input = getInput("Repos/Day1/Part1/input.txt")

processInput(c, input)

print(c.getDial())
print(c.getPass())


#data = getData(input)
#result = getResult(data)
#print(input)
#resultFile = open("result.txt", "w")
#resultFile.write(str(result))




#INTIAL TWEAKING TESTS
#c.reduce(10)
#print(c.val())
#c.increase(5)
#print(c.val())

