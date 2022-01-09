proposition = input()
#removing spaces
proposition = proposition.replace(" ", "")

operators = "^V¬>"   
letters = []
variables = {}

for i in proposition:
    if i not in operators:
        variables[i] = True
        letters.append(i)

#puting all values to make the operation

def getResult():
    result = []
    for index in range(len(proposition)):
        if proposition[index] not in operators:
            result.append(variables[proposition[index]])
        else:
            result.append(proposition[index])

    #Applying the operators
        #Not
    while "¬" in result:
        i = result.index("¬")
        result[i + 1] = not result[i + 1]  
        result.remove("¬")
        #And
    while "^" in result:
        i = result.index("^")          
        result[i - 1] = result[i - 1] and result[i + 1]
        result.remove(result[i + 1])
        result.remove("^")   
        #Or
    while "V" in result:
        i = result.index("V")          
        result[i - 1] = result[i - 1] or result[i + 1]
        result.remove(result[i + 1])
        result.remove("V")
        #Implicate
    while ">" in result:
        i = result.index(">")          
        result[i - 1] = not result[i - 1] or result[i + 1]
        result.remove(result[i + 1])
        result.remove(">")

    return result

#making the result for all possibilities.
values = [True, False]
truthTable = []
def changeValue(n):
    for i in values:
        variables[letters[n]] = i
        if n == 0:
            print(variables)
            truthTable.append(getResult())
        else:
            changeValue(n-1)
changeValue(len(variables) - 1)

print(truthTable)
