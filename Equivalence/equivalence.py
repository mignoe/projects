import functions
lastIndex = functions.lastIndex

import operators
Not_= operators.Not_
And_= operators.And_
Or_= operators.Or_
implicate = operators.implicate

input_proposition = input()
#removing spaces
input_proposition = input_proposition.replace(" ", "")


#reserved characters for the operations
reserved = ["^","V","¬",">","(",")"]   
#letters store the variables names to be accessed later
letters = []
variables = {}

#initializing the proposition's variables
for i in input_proposition:
    if i not in reserved:
        variables[i] = True
        letters.append(i)

def calculate(array):
    if "(" in array:
        indexes = functions.separate_parenthesis(array)        
        for i in indexes:          
            array[i[0]] = calculate(array[i[0] + 1:i[1]]) 
        #removing the elements left from the above operations
        for i in indexes:
            for j in range(i[0] + 1, i[1] + 1):
                array[j] = "-"
        while "-" in array:
            array.remove("-")
    array = operators.apply_operators(array, "¬", Not_)
    array = operators.apply_operators(array, "^", And_)
    array = operators.apply_operators(array, "V", Or_)
    array = operators.apply_operators(array, ">", implicate)
    return array[0]

def getResult(proposition):     
    #putting all the values on the variables
    result = []
    for i in range(len(proposition)):
        if proposition[i] not in reserved:
            result.append(variables[proposition[i]])
        else:
            result.append(proposition[i])

    return calculate(result)

#making the result for all possibilities.
values = [True, False]
truthTable = []
def changeValue(n):
    for i in values:
        variables[letters[n]] = i
        if n == 0:
            print(variables)
            truthTable.append(getResult(input_proposition))
        else:
            changeValue(n-1)
changeValue(len(variables) - 1)

print(truthTable)
