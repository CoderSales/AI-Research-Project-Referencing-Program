import nltk
import re
# open BibTex.bib
file = open("Bibtex.bib", 'r', encoding="utf8")

holder=""

line='journal={'




print(line)
print(line.startswith('journal'))
if (line.startswith('journal')):
    print('starts with journal')
    tokens = nltk.word_tokenize(line)
    print("tokens :", tokens)
    tagged = nltk.pos_tag(tokens)
    print("tagged :",tagged)
    remove_end = tagged[0:-2] # cut space and last curly bracket
    print("remove_end :", remove_end)
    # for line in remove_end:
    for k,line in enumerate(remove_end, start = 1):
        print('hi')
        print("line[k] :", line[k])
        print("remove_end :", remove_end)
        if(line[k]!=len(remove_end)): # remove_end may be line instead
            holder+=line[0]+' '
        else:
            holder+=line[0]
        if(re.search('^journal',holder)):
            start_after_journal=slice(len_journal,None,1)
            no_journal=holder[start_after_journal]

# uncomment
# only works if no_journal exists:
if no_journal!=None:
    print(no_journal)








# pass something from BibTex.bib in here:
# for k,v in enumerate(remove_end, start = 1):

