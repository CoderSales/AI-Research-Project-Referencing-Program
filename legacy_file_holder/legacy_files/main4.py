import nltk
import re
# open BibTex.bib
file = open("Bibtex.bib", 'r', encoding="utf8")

holder=""

line='journal={'




print(line)
print(line.startswith('journal'))

len_journal=len('journal={')


for line in file:

    if (line.startswith('journal')):
        print('starts with journal')
        tokens = nltk.word_tokenize(line)
        print("tokens :", tokens)
        tagged = nltk.pos_tag(tokens)
        print("tagged :",tagged)
        remove_end = tagged[0:-2] # cut space and last curly bracket
        print("remove_end :", remove_end)
        # for line in remove_end:
        for k,line in enumerate(remove_end, start = 0):
            print("line[0] :", line[0])
            print("remove_end :", remove_end)
            if(line[0]!=len(remove_end)): # remove_end may be line instead
                holder+=line[0]+' '
            else:
                holder+=line[0]
            print('line 34 is last line out')
            if(re.search('^journal',holder)):
                start_after_journal=slice(len_journal,None,1)
                no_journal=holder[start_after_journal]
            print('line 38 is not accessed')

# uncomment
# only works if no_journal exists:
if no_journal!=None:
    print(no_journal)








# pass something from BibTex.bib in here:
# for k,v in enumerate(remove_end, start = 1):

