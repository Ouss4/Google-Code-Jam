
fileName = "B-large-practice.in"
with open(fileName, "r") as inputFile:
    i = 1
    # Read the file and remove the first element and the last \n
    fileContent = inputFile.read().split("\n")[1:-1] 

    for line in fileContent:
        print("Case #{}: {}".format(i, " ".join(line.split()[::-1])))
        i += 1
        
