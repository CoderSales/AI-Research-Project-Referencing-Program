import nltk 
nltk.download('punkt')

import re

file = open("Bibtex.bib", 'r', encoding="utf8")

holder=""

line='journal={'
no_journal=None

if (re.search('^journal',line)):
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)
    remove_end = tagged[0:-2] # cut space and last curly bracket
    for k, line in enumerate(remove_end, start=0):
        if(line[k]!=len(remove_end)):
            holder+=line[0]+' '
        else:
            holder+=line[0]
        if(re.search('^journal',holder)):
            start_after_journal=slice(line,None,1)
            no_journal=holder[start_after_journal]

# uncomment
# only works if no_journal exists:
if no_journal!=None:
    print(no_journal)
