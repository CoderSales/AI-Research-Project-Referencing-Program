def firstinitial(allnames):

    firstInitialIndices=[]
 
    for letterIndex, letter in enumerate(allnames):

        commaIndex=(letterIndex-2)
        spaceIndex=(letterIndex-1)

        if (allnames[commaIndex]==','): # print('comma 2 ago')
            if (allnames[spaceIndex]==' '): # print('space one ago')
                # print('letterIndex',letterIndex)
                firstInitialIndices.append(letterIndex)
                # print(firstInitialIndices)
                # firstinitial=allnames[0]
    return firstInitialIndices
