def toT9(text):

    translator = {0: ' ', 2:'abc', 3:'def', 4:'ghi', 5:'jkl',
                  6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
                  
    output = ""
    oldKey = -1

    for c in text:
        for key, val in translator.items():
            i = val.find(c) + 1
            if i > 0:
                if oldKey == key:
                    output += " "
                output += str(key) * i
                oldKey = key
    return output


fileName = "small.txt"
with open(fileName, "r") as inputFile:
    i = 1
    # Read the file and remove the first element and the last \n
    fileContent = inputFile.read().split("\n")[1:-1] 

    for text in fileContent:
        t9Text = toT9(text)
        print("Case #{}: {}".format(i, t9Text))
        i += 1
        
