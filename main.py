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

reference = author + ' (' + year + ') ' + '\'' + title + '\'' + ',' + ' ' + journal + ',' + ' ' + volume + '(' + number + ')' + ' ' + 'pp. ' + pages + ', ' + 'available: ' + doi + ' / ' + url + ' [accessed: ' + date + '].'

print(reference)
