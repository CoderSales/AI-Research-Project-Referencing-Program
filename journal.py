# import numpy
# import pandas
# import openpyxl
from openpyxl import Workbook
import datetime
import os
import shutil
import os.path

import nltk

# import parser1

import re

# parser1.parse()

your_path = os.environ.get("PWD")
root = your_path
files = [(path,f) for path,_,file_list in os.walk(root) for f in file_list]
f_name="Bibtex.bib"
from shutil import copy
# f = open(os.path.join(your_path, f_name), 'r', encoding="utf8")
# for i in f.readlines():
#     print(i)
# f.close()

file = open("Bibtex.bib", 'r', encoding="utf8")

holder=""
len_journal=len('journal={')
for line in file:
    if (re.search('^journal',line)):
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        remove_end = tagged[0:-2] # cut space and last curly bracket
        for k,line in enumerate(remove_end, start = 0):
            # print("line 38: line[0] =", line[0])
            if(line[0]!=len(remove_end)): # remove_end may be line instead
                holder+=line[0]+' '
            else:
                holder+=line[0]
            if(re.search('^journal',holder)):
                start_after_journal=slice(len_journal,None,1)
                no_journal=holder[start_after_journal]

no_journal

tokens_no_journal = nltk.word_tokenize(no_journal)
tagged_tokens_no_journal = nltk.pos_tag(tokens_no_journal)
no_journal_minus_starting_curly_bracket = tagged_tokens_no_journal[1:] # cut space and last curly bracket

holder2=''

list_of_keys=[]
for k3,v3 in no_journal_minus_starting_curly_bracket:
    list_of_keys.append(k3)

# print 1 of 3:
# print('line 65: list_of_keys',list_of_keys) # keys to tokens # ['Software', ',', 'practice', '&', 'experience']

for k2,v2 in enumerate(no_journal_minus_starting_curly_bracket):
    if (k2!=len(list_of_keys)):
        if (k2+1!=len(list_of_keys)): # avoids index out of range error
            print('line 65:',list_of_keys[k2+1])

            # so, if the next one IS a comma, and not this one:
            if(v2 != ',' and list_of_keys[k2+1]==','): # if this isn't but next element is a comma:
                
                print('\n', 'line 70: start of 1 off block for comma next',sep="")
                print('line 71: (k2) :',k2)
                print('line 72: (v2), list_of_keys[k2+1]:',v2, list_of_keys[k2+1])
                print('line 73: so, list_of_keys[k2+1] = ', list_of_keys[k2+1])
                
                holder2 += v2[0] # wait, save space for next element coming in.
                print('line 76: holder2',holder2)

                print('line 78: end of 1 off block for comma next', '\n')

            # then, if neither this nor next:
            # no commas in sight:

            elif(v2 != ',' and list_of_keys[k2+1]!=','): # if this element is not a comma, and neither is next:
                # (and if this is not the last, which it can't be due to precondition for loop)
                holder2 += v2[0] + ' ' # then can add a space
                
                # print 2 of 3:
                print('line 88: holder2', holder2)
            # and, if it's not a comma
        elif(k2+1 == len(list_of_keys)):
            holder2 += v2[0] # experience

    else:
        # no space if last element
        holder2+=v2[0]
# print 3 of 3:
print('line 97: (post last for-if, which assembles holder2) holder2:', holder2 )
