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

def spacesInAuthorString(allnames):
    
    spacesList = []

    for letterIndex, letter in enumerate(allnames):
        
        if letter==' ':
            spacesList.append(letterIndex)

    return spacesList

# import firstname
# allnames=firstname.allnames()
# spacesInAuthorString=spacesInAuthorString(allnames)
# print(spacesInAuthorString)
