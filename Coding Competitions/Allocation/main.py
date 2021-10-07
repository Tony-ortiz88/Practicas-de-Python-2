from math import *

def validateFile(file, numOfCredit):
    filein = file
    num = 0

    for i in filein:
        i = i.rstrip("\n")
        i = i.split(' ')
            #lines[x].append()
        #line = i.split(' ')
        lines.append(i)
        num += 1


    if(((num)/2) == float(numOfCredit)):
        return True
    else:
        return False

def Calculate(file):
    filein = file
    count = 0
    acum = 0
    output = []
    case = 0


    for i in range(1, len(file), 2):
        case += 1
        file[i].sort()
        for x in range(0, int(file[i - 1][0])):
            acum += int(file[i][x])
            if(acum <= int (file[i - 1][1])):
                count+=1
            else:
                str = "Case #{0}: {1}".format(case, count)
                output.append(str)
                acum = 0
                count = 0
                break
    writeFile(output)


def readFile():
    global f
    global lines
    numOfcredi = f.readline()
    if(validateFile(f, numOfcredi) == True):
        Calculate(lines)


    f.close()
def writeFile(output):
    # outputFile = open('output.txt', "w")
    # print(output)
    for x in output:
        print(x)
    #     outputFile.writelines(x +'\n')
    # outputFile.close()



lines = []

def main():

    readFile()
    ##writeFile()

if __name__ == '__main__':
    f = open('intput.txt')
    main()