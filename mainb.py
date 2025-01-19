"""
This file calls:
- author
- journal

function inside
file
for each
"""

#_____________________________________

import count

# count.count()

# ____________________________________

import lines

from lines import author

author=author.author()

# ___________________________________

import lines

from lines import year

year=year.year()

# __________________________________

import lines

from lines import title

title=title.title()

# __________________________________

import lines

from lines import journal

journal=journal.journal()

# ___________________________________

import lines

from lines import volume

volume=volume.volume()

# __________________________________

import lines

from lines import number

number=number.number()

# __________________________________

import lines

from lines import pages

pages=pages.pages()


# __________________________________

import lines

from lines import url

url=url.url()


# __________________________________

import lines

from lines import doi

doi=doi.doi()


# __________________________________

import date

date=date.date()

# __________________________________

import andReplacer

andReplacer = andReplacer.andReplacer()

# __________________________________

from linesRis import risL1 

risL1 = risL1.risL1()

# __________________________________

# note on import of last or each module above: 
# import module (file), then do
# imported_module.the_function_in_the_imported_module()
# and set the name previously used for the module to be the_function_from_the_module

# __________________________________

# can use either of the following lines:

reference1 = "\n" + "TY - " + "" + "\n" + "TI - " + title + "\n" + "DO - " + doi + "\n" + "UR - " + url + "\n" + "AU - " + author + "\n" + "PY - " + "" + "\n" + "VL - " + volume + "\n" + "M3 - " + risL1 + "\n" + "ER - " + ""

# author + ' (' + year + ') ' + + ' ' + journal + ',' + ' ' + volume + '(' + number + ')' + ' ' + 'pp. ' + pages + ', ' + 'available: ' + doi + ' / ' + url + ' [accessed ' + date + '].'


# reference = andReplacer.andReplacer()

# print("title =", title)
# print("journal", journal)
# print("\ncheckpoint\n")
# print(',')
# print(' ')
# print("volume = ", volume)
# print('(')
# print(number)
# print("\ncheckpoint\n")


print(reference1)
