# import firstname # has allnames
# allnames=firstname.allnames()
# import firstname2 # has spacesInAuthorString
def checkIfFirstNameBetweenSpaces(firstname, firstname2, allnames):
    spacesList=firstname2.spacesInAuthorString(allnames)
    # import useSpacesInAuthorString
    # spacesList
    
    for spaceIndex, space in enumerate(spacesList):
        new=''
        if(spaceIndex!=0):
            spaceLastIndex = spaceIndex-1
            spaceNextIndex = spaceIndex
            import firstname2
            firstInitialIndices=firstname2.firstinitial(allnames)
            for letterIndex in firstInitialIndices:
                if letterIndex <spaceNextIndex and letterIndex > spaceLastIndex:
                    startLetterIndex=letterIndex
                    endLetterIndex=spaceNextIndex-1
                    endLetterIndexRule=endLetterIndex+1
                    if letterIndex != startLetterIndex:
                        # for firstNameLetter in allnames.slice[startLetter,endLetterIndexRule]:
                            # firstNameLetter.replace('_'):
                        import TestFromIndicesGetChar
                        characterList = TestFromIndicesGetChar.getCharFromIndices(allnames)
                        import firstnameinitialscaller
                        firstInitialIndices = firstnameinitialscaller.firstNameInitialsCaller()
                        for characterIndex, character in zip(firstInitialIndices,characterList):
                            allnames.strip(startLetterIndex,endLetterIndexRule).replace(allnames.strip(startLetterIndex,endLetterIndexRule),allnames[startLetterIndex])
                            allnames=allnames.strip(0,startLetterIndex)+allnames.strip(startLetterIndex,(startLetterIndex+1))+allnames.strip((startLetterIndex+1),-1)
                            new = allnames.strip(startLetterIndex,endLetterIndexRule)
                            # return spacesList
                        return allnames

# print(checkIfFirstNameBetweenSpaces())

def getNameNumbers():
    import firstname # has allnames
    # import firstname # has allnames
    allnames=firstname.allnames()
    import firstname2 # has spacesInAuthorString
    spacesList=firstname2.spacesInAuthorString(allnames)
    indivNames=allnames.split(' ')
    return indivNames 

# indivNames=getNameNumbers()
# print(indivNames)
