import functions

proposition = "x>y"

functions = {
    "^": functions.And,
    "V": functions.Or,
    "¬": functions.Not,
    ">": functions.implicate
        }
variables = {}
for i in proposition:
    if i not in functions:
        variables[i] = True

#making everything happen
resultado = ""
def result():
    for i in range(len(proposition)):
        if proposition[i] in functions:
            operator = functions[proposition[i]]
            firstVar = variables[proposition[i - 1]]
            secondVar = variables[proposition[i + 1 ]]
            aux = operator(firstVar, secondVar)
            print(aux)
        
def changer():
    for i in variables:
        if variables[i] == False:
            variables[i] = True
            break






