Exception has occurred: AttributeError
'list' object has no attribute 'keys'
  File "~\journal2.py", line 15, in <module>
    tagged_keys = tagged.keys()
                  ^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'keys'

how to get keys from tuple python
Yahoo
https://uk.search.yahoo.com/search?fr=mcafee&type=E210IE1274G0&p=how+to+get+keys+from+tuple+python

https://www.geeksforgeeks.org/python-get-all-tuple-keys-from-dictionary/

extract from tuple
Yahoo
https://uk.search.yahoo.com/search?fr=mcafee&type=E210IE1274G0&p=extract+from+tuple

____

```python
# Python3 code to study about
# unpacking python tuple using *

# first and last will be assigned to x and z
# remaining will be assigned to y
x, *y, z = (10, "Geeks ", " for ", "Geeks ", 50)

# print details
print(x)
print(y)
print(z)

# first and second will be assigned to x and y
# remaining will be assigned to z
x, y, *z = (10, "Geeks ", " for ", "Geeks ", 50)
print(x)
print(y)
print(z)
```

https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/

____

Part 2:

____

Yahoo
unpack list
https://uk.search.yahoo.com/search?fr=mcafee&type=E210IE1274G0&p=unpack+list

____

Result 1 from last reference:

```python
colors = ['red', 'blue', 'green']
```

To assign the first, second, and third elements of the list to variables, you may assign individual elements to variables like this:

```python
red = colors[0]
blue = colors[1]
green = colors[2]
```

https://www.pythontutorial.net/python-basics/python-unpack-list/


_________


## Debugging converting first names to initials bug

testcheckSpacesAuthorList.py", line 117
    firstLetterListRebuiltAgain = callerOfManyFirstLetters( allnames )

testcheckSpacesAuthorList.py", line 114, in callerOfManyFirstLetters
	firstLetterTest=getFirstLetter(firstnames, index)

testcheckSpacesAuthorList.py", line 104, in getFirstLetter        
    initial=x[index] # Potential Fix: for single firstname returned only in testSquaredcSAL.py: Q/Command: Replace: `initial=x[0]` `0`with `index`

IndexError: string index out of range

########

index on 104 out of range
what is range?

what is x?
x is Dirk was Gunter

so poss 2 is len

so index of 4 maybe is out of range?

_____
