# imports

import nltk
import re

# file

f_name="Bibtex.bib"
file = open("Bibtex.bib", 'r', encoding="utf8")

# end prep

holder=""
count=1
lines=1
file1=file
for line1 in file1:
    lines=lines+1
    
print(lines, "lines in BibTex.bib")

endline=''
file = open("Bibtex.bib", 'r', encoding="utf8")
for line in file:
    if (re.search('^journal',line)):
        starter=line
        line=line.lstrip('journal = {')
        line=line.rstrip('},\n')

        endline=line
print(endline)