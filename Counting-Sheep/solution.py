  
def checkNumber(N):
    i = 1
    digitsBool = [False] * 10
    done = False
    numbers = "0123456789"
    nextNumber = i*N
    
    while(not done):
        for digit in nextNumber:
            if digit in numbers:
                digitsBool[ord(digit) - ord("0")] = True
                
        if digitsBool == [True] * 10:
            done = True
            result = (True, nextNumber)
        
        else:
            i += 1
            nextNumber = str(i*int(N))
            if(nextNumber == N):
                done = True
                result = (False, "INSOMNIA")
            
    return result

fileName = "A-large-practice.in"
with open(fileName, "r") as inputFile:
    i = 1
    # Read the file and remove the first element and the last \n
    fileContent = inputFile.read().split("\n")[1:-1] 

    for number in fileContent:
        result = checkNumber(number)
        print("Case #{}: {}".format(i, result[1]))
        i += 1
