# def journal():
#     """
#     reads BibTex.bib file
#     outputs
#     journal name
#     """



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

lines=1
file1=file
for line1 in file1:
    lines=lines+1
    
print(lines, "lines in BibTex.bib")

endline=''
file = opener(f_name)
for line in file:
    if (re.search('^journal',line)):
        starter=line
        line=line.lstrip('journal = {')
        line=line.rstrip('},\n')

        endline=line
print(endline)
