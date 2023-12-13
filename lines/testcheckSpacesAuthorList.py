import checkSpacesAuthorList

import firstname # has allnames
allnames=firstname.allnames()
import firstname2 # has spacesInAuthorString

checkIfFirstNameBetweenSpaces=checkSpacesAuthorList.checkIfFirstNameBetweenSpaces(firstname, firstname2, allnames)

getNameNumbers=checkSpacesAuthorList.getNameNumbers() # ['Kniesel,', 'Günter', 'and', 'Theisen,', 'Dirk']

def ifHasComma(getNameNumbers):
    firstnames=[]
    for name in getNameNumbers:
        if name != 'and':
            if ',' not in name:
                firstnames.append(name)
    return firstnames

firstnames=ifHasComma(getNameNumbers)
print('line 20 : ifHasComma() returns: firstnames :', firstnames)

def returnallnames(firstnames):
    firstnames
    return firstnames # ['Günter', 'Dirk']

allfirstnames=returnallnames(firstnames)

def getOneName(allfirstnames, index):
    firstname1=allfirstnames[index]
    return firstname1

# def getRangeOfLenOfallfirstnamesList(allfirstnames, index):
def getRangeOfLenOfallfirstnamesList(allfirstnames):
    lenFirstNameList=len(allfirstnames)
    indicesOfFirstNameList=range(lenFirstNameList)
    # for index in indicesOfFirstNameList:
    #     if 
    #     firstname1=getOneName(allfirstnames, index)
    return indicesOfFirstNameList

def getTheOneFirstnameSpecified(allfirstnames, index3):
    rangeOfLenOfallfirstnamesList=getRangeOfLenOfallfirstnamesList(allfirstnames)
    # for index2 in rangeOfLenOfallfirstnamesList:
    #     allfirstnames[index2]
    itemFromallfirstnames=allfirstnames[index3]
    return itemFromallfirstnames

def goThroughallfirstnamesRecompileList(allfirstnames):
    rangeOfLenOfallfirstnamesList=getRangeOfLenOfallfirstnamesList(allfirstnames)
    listOfFirstNamesRecompiled=[]
    for index2 in rangeOfLenOfallfirstnamesList:
        currentFirstname=allfirstnames[index2]
        listOfFirstNamesRecompiled.append(currentFirstname)
    # itemFromallfirstnames=allfirstnames[index3]
    # return itemFromallfirstnames
    return listOfFirstNamesRecompiled

recompiledFirstnameList=goThroughallfirstnamesRecompileList(allfirstnames)
print('line 59: goThroughallfirstnamesRecompileList() returns: recompiledFirstnameList :',recompiledFirstnameList)

# def getSingleInstanceFromAList(allfirstnames, index):
def getSingleInstanceFromAList(allfirstnames):
    lenFirstNameList=len(allfirstnames)
    indicesOfFirstNameList=range(lenFirstNameList)
    # for index in indicesOfFirstNameList:
    #     if 
    #     firstname1=getOneName(allfirstnames, index)
    return indicesOfFirstNameList

indicesOfFirstNameList = getSingleInstanceFromAList(allfirstnames)


print('line 73 :',)

# wanna get:
# a single instance
# from a list
def rebuildAllInstances(allfirstnames):
    rebuildFirstNamesList=[]
    for index1, eachInstance in enumerate(allfirstnames):
        # aRange=getSingleInstanceFromAList(allfirstnames, index1)
        aRange=getSingleInstanceFromAList(allfirstnames)
        rebuildFirstNamesList.append(allfirstnames[index1])
    return rebuildFirstNamesList

rebuiltFirstNamesList = rebuildAllInstances(allfirstnames)

def getFirstLetter(allnames):
    allnames=returnallnames(allnames)
    for x in allnames: # x ~= Gunter
        initial=x[0]
    return initial # ['Günter', 'Dirk']

getFirstLetter(firstnames)
def replaceFirstNameWithInitial(allnames):
    allnames
    return allnames # ['Günter', 'Dirk']

replaceFirstNameWithInitial(allnames)
