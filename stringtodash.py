# This file will convert string characters to underscores

def lenstr(convString):
    langth = len(convString)
    print('langth is: ', langth)
    return(langth)
    
def dash(undScore):
    arrayUndscore = []
    for char in range(undScore):
        arrayUndscore.append('_')

    print(''.join(arrayUndscore))


lengt = lenstr('Hello')
dash(lengt)


