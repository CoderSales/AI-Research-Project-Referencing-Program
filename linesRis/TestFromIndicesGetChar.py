def importForGetChar():
    # import module:

    import firstname

    # locally name function(s):

    allnames = firstname.allnames()

    # firstinitial = firstinitial(allnames)

    # define function:
    return allnames

allnames = importForGetChar()

def getCharFromIndices(allnames):


    import firstnameinitialscaller

    firstNameInitialsCaller = firstnameinitialscaller.firstNameInitialsCaller()

    fNIC = firstNameInitialsCaller


    characterList = []


    for index in fNIC:
        # print(index)
        aCharacter = allnames[index]
        characterList.append(aCharacter)



    return characterList

# getCharFromIndices = getCharFromIndices(allnames)
# print(getCharFromIndices)
