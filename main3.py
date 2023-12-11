import nltk
import re

file = open("Bibtex.bib", 'r', encoding="utf8")

holder=""

line='journal={'

if (re.search('^journal',line)):
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)
    remove_end = tagged[0:-2] # cut space and last curly bracket
    for line in remove_end:
        if(x[position]!=length(whatever_passed_in_string)):
            holder+=line[0]+' '
        else:
            holder+=line[0]
        if(re.search('^journal',holder)):
            start_after_journal=slice(len_journal,None,1)
            no_journal=holder[start_after_journal]

print(no_journal)
