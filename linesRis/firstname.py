def allnames():
    import names3

    names3=names3.names3()
    return names3
# allnames=allnames() #
# print('allnames:', allnames)

def firstinitial(allnames):
    # import firstname
    # firstname=firstname.firstname()
    # firstname=firstname()
    firstInitialIndices=[]
    # print('line 13: allnames:', allnames)#
    # print(allnames[7]==',')#
    for letterIndex, letter in enumerate(allnames):
        # print('letter', letterIndex, 'is:', letter)
        commaIndex=(letterIndex-2)
        spaceIndex=(letterIndex-1)
        # print('test:')
        # print(allnames[commaIndex])
        if (allnames[commaIndex]==','):
        # if ((letterIndex-2)=='/,'):
            # print('comma 2 ago')
            if (allnames[spaceIndex]==' '):
                # print('space one ago')
                # print('letterIndex',letterIndex)
                firstInitialIndices
                # firstinitial=allnames[0]
    return firstInitialIndices

# firstinitial=firstinitial(allnames)#
# print('firstinitial',firstinitial)#

def checkForComma(allnames):
    import nltk
    tokens = nltk.word_tokenize(allnames)
    commaIndexes=[]
    for i, char in enumerate(allnames):
        if char == ',':
            print(',')
            commaIndexes.append(i)
    return commaIndexes

# checkForComma = checkForComma(allnames)#
# print(checkForComma)#

def printFromCommaIndex(allnames, checkForComma):
    """
    input arguments:
    
    - aString:
    allnames

    - checkForComma:
    (variable (type:list))
    takes a list of commas
    returned from checkForComma
    and called and saved to
    variable checkForComma

    output:
    returns 
    charAtEachCommaIndex
    """
    
    

    return charAtEachCommaIndex
