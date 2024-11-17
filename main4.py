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

reference = author + ' (' + year + ') ' + '\'' + title + '\'' + ',' + ' ' + journal + ',' + ' ' + volume + '(' + number + ')' + ' ' + 'pp. ' + pages + ', ' + 'available: ' + doi + ' / ' + url + ' [accessed ' + date + '].'

# print("author =", author)
# print(' (')
# print("year =", year )
# print(') ')
# print("checkpoint");
# print('\'')
print("title =", title)
# print('\'')
# print(',')
# print(' ')
# print("checkpoint");
print("journal", journal)
print("\ncheckpoint\n")
print(',')
print(' ')
print("volume = ", volume)
print('(')
print(number)
print("\ncheckpoint\n")
# print(')')
# print("checkpoint");
# print(' ')
# print('pp. ')
# print("pages =",pages)
# print(', ')
# print('available: ')
# print("checkpoint")
# print("doi =", doi)
# print(' / ')
# print("url = ", url)
# print(' [accessed ')
# print("date =", date)
# print('].')


print(reference)
