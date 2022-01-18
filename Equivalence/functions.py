def lastIndex(array, value):
    if value in array:
        index = 0
        for i in range(len(array)):
            if array[i] == value:
                index = i
        return index

def separate_parenthesis(array):
    opening_parenthesis = False
    inside_parenthesis = False
    indexes = []
    parenthesis_indexes = []
    
    for i in range(len(array)):
        if not opening_parenthesis and array[i] == "(":     
            opening_parenthesis = True
            parenthesis_indexes.append(i)
        elif opening_parenthesis and array[i] == "(":
            inside_parenthesis = True
        elif inside_parenthesis and array[i] == ")":
            inside_parenthesis = False
        elif not inside_parenthesis and array[i] == ")":
            opening_parenthesis = False
            parenthesis_indexes.append(i)
            indexes.append(parenthesis_indexes)
            parenthesis_indexes = []
            
    
    return indexes

#print(separate_parenthesis("( x V y ) V ¬ ( x V y )".split()))



