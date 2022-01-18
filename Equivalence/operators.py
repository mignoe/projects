def Not_(bool):
    return not bool
Not_.arguments = 1
def And_(bool1, bool2):
    return bool1 and bool2
And_.arguments = 2
def Or_(bool1, bool2):
    return bool1 or bool2
Or_.arguments = 2
def implicate(bool1, bool2):
    return not bool1 or bool2
implicate.arguments = 2

def apply_operators(array, str, function):
    while str in array:
        i = array.index(str)          
        if function.arguments == 1:
            array[i] = function(array[i+1])
            array.remove(array[i+1])
        elif function.arguments == 2:
            array[i - 1] = function(array[i - 1], array[i + 1])
            array.remove(array[i + 1])
            array.remove(str)   
    return array

