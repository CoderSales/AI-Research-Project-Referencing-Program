"""
This file calls:
- author
- journal

function inside
file
for each
"""

""""
(CoderSales)

https://github.com/CoderSales
"""

"""
MIT License

Copyright (c) 2023 Stephen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# ____________________________________

def author():
    """
    encapsulate author program in a
    function
    """
    # imports

    import nltk
    import re

    # file

    f_name="BibTex.bib"

    def opener(f_name):
        file = open(f_name, 'r', encoding="utf8")
        return file

    file=opener(f_name)

    # end prep

    endline=''
    file = opener(f_name)
    for line in file:
        if (re.search('^author',line)):
            starter=line
            line=line.lstrip('author = {')
            line=line.rstrip('},\n')

            endline=line
    # print(endline)
    return endline
# author=author()
# print(author)

author=author()

# ___________________________________

def year():
    """
    encapsulate author program in a
    function
    """
    # imports

    import nltk
    import re

    # file

    f_name="BibTex.bib"

    def opener(f_name):
        file = open(f_name, 'r', encoding="utf8")
        return file

    file=opener(f_name)

    # end prep

    endline=''
    file = opener(f_name)
    for line in file:
        if (re.search('^year',line)):
            starter=line
            line=line.lstrip('year = {')
            line=line.rstrip('},\n')

            endline=line
    # print(endline)
    return endline


year=year()

# __________________________________

def title():
    """
    encapsulate author program in a
    function
    """
    # imports

    import nltk
    import re

    # file

    f_name="BibTex.bib"

    def opener(f_name):
        file = open(f_name, 'r', encoding="utf8")
        return file

    file=opener(f_name)

    # end prep

    endline=''
    file = opener(f_name)
    for line in file:
        if (re.search('^title',line)):
            starter=line
            line=line.lstrip('title = {')
            line=line.rstrip('},\n')

            endline=line
    # print(endline)
    return endline

title=title()

# __________________________________

def journal():
    """
    reads BibTex.bib file
    outputs
    journal name
    """



    # imports

    import nltk
    import re

    # file

    f_name="BibTex.bib"

    def opener(f_name):
        file = open(f_name, 'r', encoding="utf8")
        return file

    file=opener(f_name)

    # end prep

    endline=''
    file = opener(f_name)
    for line in file:
        if (re.search('^journal',line)):
            starter=line
            line=line.lstrip('journal = {')
            line=line.rstrip('},\n')

            endline=line
    # print(endline)
    return endline

journal=journal()

# ___________________________________

def volume():
    """
    encapsulate author program in a
    function
    """
    # imports

    import nltk
    import re

    # file

    f_name="BibTex.bib"

    def opener(f_name):
        file = open(f_name, 'r', encoding="utf8")
        return file

    file=opener(f_name)

    # end prep

    endline=''
    file = opener(f_name)
    for line in file:
        if (re.search('^volume',line)):
            starter=line
            line=line.lstrip('volume = {')
            line=line.rstrip('},\n')

            endline=line
    # print(endline)
    return endline

volume=volume()

# __________________________________

def number():
    """
    encapsulate author program in a
    function
    """
    # imports

    import nltk
    import re

    # file

    f_name="BibTex.bib"

    def opener(f_name):
        file = open(f_name, 'r', encoding="utf8")
        return file

    file=opener(f_name)

    # end prep

    endline=''
    file = opener(f_name)
    for line in file:
        if (re.search('^number',line)):
            starter=line
            line=line.lstrip('number = {')
            line=line.rstrip('},\n')

            endline=line
    # print(endline)
    return endline

number=number()

# __________________________________

def pages():
    """
    encapsulate author program in a
    function
    """
    # imports

    import nltk
    import re

    # file

    f_name="BibTex.bib"

    def opener(f_name):
        file = open(f_name, 'r', encoding="utf8")
        return file

    file=opener(f_name)

    # end prep

    endline=''
    file = opener(f_name)
    for line in file:
        if (re.search('^pages',line)):
            starter=line
            line=line.lstrip('pages = {')
            line=line.rstrip('},\n')

            endline=line
    # print(endline)
    return endline

pages=pages()

# __________________________________

def date():
    """
    get today's date
    """

    # Import date class from datetime module
    from datetime import date

    # Returns the current local date
    today = date.today()
    # print("Today date is: ", today)
    today=str(today)
    return today

date=date()

# __________________________________

reference = author + ' (' + year + ') ' + '\'' + title + '\'' + ',' + ' ' + journal + ',' + ' ' + volume + '(' + number + ')' + ' ' + 'pp. ' + pages + ', ' + 'available: ' + '[accessed: ' + date + '].'

print(reference)
