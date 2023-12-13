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
# print('line 20 : ifHasComma() returns: firstnames :', firstnames)

def getfirstnames(getNameNumbers):
    """
    for firstnames variable before this function 
    to be available in other files
    """
    firstnames=ifHasComma(getNameNumbers)
    return firstnames

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

# recompiledFirstnameList=goThroughallfirstnamesRecompileList(allfirstnames)
# print('line 59: goThroughallfirstnamesRecompileList() returns: recompiledFirstnameList :',recompiledFirstnameList)

# def getSingleInstanceFromAList(allfirstnames, index):
def getSingleInstanceFromAList(allfirstnames):
    lenFirstNameList=len(allfirstnames)
    indicesOfFirstNameList=range(lenFirstNameList)
    # for index in indicesOfFirstNameList:
    #     if 
    #     firstname1=getOneName(allfirstnames, index)
    return indicesOfFirstNameList

indicesOfFirstNameList = getSingleInstanceFromAList(allfirstnames)


# print('line 73 :',)

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

####################################

def getFirstLetter(allnames, index):
    allnames=returnallnames(allnames)
    print('tcSAL 100: allnames, len',allnames, len(allnames))
    for firstname2 in allnames: # firstname2 ~= Gunter
        # print('tcSAL 102 firstname2:',firstname2)
        # print('tcSAL 102 index:',index)
        listofinitials=[]
        if index<=len(allnames):
            print(index, ' is less than ', len(allnames))
            print('tcSAL 105 index:',index)
            print('tcSAL 106 firstname2:',firstname2)
            print('tcSAL 107 len(firstname2): ', len(firstname2))
            initial=firstname2[index] # Potential Fix: for single firstname returned only in testSquaredcSAL.py: Q/Command: Replace: `initial=x[0]` `0`with `index`
            print('tcSAL 109 initial:',initial)
            listofinitials.append(initial)
    return listofinitials # ['Günter', 'Dirk']
def callerOfManyFirstLetters(allnames):
    firstLetterListRebuiltAgain=[]
    lenallnames=len(allnames)
    ranlenallnames=range(lenallnames)
    list=[]
    for index in ranlenallnames:
        firstLetterListRebuiltAgain.append(index) # issue? Q/ get item at index? what's that? A/ allnames[index] Q/Command: no replace list with firstLetterListRebuiltAgain
        firstLetterTest=getFirstLetter(firstnames, index)
        list.append(firstLetterTest)
    return [list, firstLetterListRebuiltAgain]
firstLetterListRebuiltAgain=callerOfManyFirstLetters(allnames)
print('line 111: firstLetterListRebuiltAgain:', firstLetterListRebuiltAgain) # Bug: list from 0 to 32
# line 111: firstLetterListRebuiltAgain: [[['D'], ['i'], ['r'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]]

#########################################

def replaceFirstNameWithInitial(allnames):
    allnames
    return allnames # ['Günter', 'Dirk']

replaceFirstNameWithInitial(allnames)
