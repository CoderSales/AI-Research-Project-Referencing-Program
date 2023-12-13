# dependencies:

import checkSpacesAuthorList

import firstname # has allnames
allnames=firstname.allnames()
import firstname2 # has spacesInAuthorString

# validate dependencies imported

checkIfFirstNameBetweenSpaces=checkSpacesAuthorList.checkIfFirstNameBetweenSpaces(firstname, firstname2, allnames)

getNameNumbers=checkSpacesAuthorList.getNameNumbers() # ['Kniesel,', 'Günter', 'and', 'Theisen,', 'Dirk']

# imports:


import testcheckSpacesAuthorList

ifHasComma=testcheckSpacesAuthorList.ifHasComma(getNameNumbers)

firstnames= testcheckSpacesAuthorList.ifHasComma(getNameNumbers) # problem

################################

firstnames=testcheckSpacesAuthorList.returnallnames(firstnames) # ['Günter', 'Dirk']

# # # # # # # #

firstnames1=testcheckSpacesAuthorList.returnallnames(firstnames) # ['Günter', 'Dirk']

# # # # # # # #

allfirstnames=testcheckSpacesAuthorList.returnallnames(firstnames) # ['Günter', 'Dirk']

# # # # # # # # 

import testcheckSpacesAuthorList as tcSAL

# for calling getOneName from testcheckSpacesAuthorList (.py) :

def firstnamesRebuilder(allfirstnames):
    firstnamesRebuild=[]
    rangeLenAllfirstnames=range(len(allfirstnames))
    for index in rangeLenAllfirstnames:
        firstname1=tcSAL.getOneName(allfirstnames, index)
        firstnamesRebuild.append(firstname1)
    return firstnamesRebuild

firstnamesRebuilt=firstnamesRebuilder(allfirstnames)

print(firstnamesRebuilt) # ['Günter'] # Why not other name? # initial=x[0] has static index 0 only on line 99 of testcheckSpacesAuthorList.py
# now: from testcheckSpacesAuthorList.py: line 101: initial=x[index] # Potential Fix: for single firstname returned only in testSquaredcSAL.py: Q/Command: Replace: `initial=x[0]` `0`with `index`

