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
            print("line 38: line[0] =", line[0])
            # print("line[0] :", line[0])
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
# print("line 55 (pre last for-loop-if-else-combination) : no_journal_minus_starting_curly_bracket :", no_journal_minus_starting_curly_bracket)

list_of_keys=[]
for k3,v3 in no_journal_minus_starting_curly_bracket:
    list_of_keys.append(k3)
print('line 65: list_of_keys',list_of_keys) # keys to tokens

for k2,v2 in enumerate(no_journal_minus_starting_curly_bracket):
    if (k2!=len(no_journal_minus_starting_curly_bracket)):
        # print('line 64 repeats: length of this loop is:', len(no_journal_minus_starting_curly_bracket)) # length is 5
        if (k2+1!=len(no_journal_minus_starting_curly_bracket)): # avoids index out of range error
            if(v2 !=',' and no_journal_minus_starting_curly_bracket[k2+1]==','): # if this isn't but next element is a comma:
                holder2+=v2[0] # wait, save space for next element coming in.
                print('line 67: holder2',holder2)
            elif(v2!=',' and no_journal_minus_starting_curly_bracket[k2+1]!=','): # if this element is not a comma, and neither is next:
                # (and if this is not the last, which it can't be due to precondition for loop)
                holder2+=v2[0] + ' ' # then can add a space
                print('line 71: holder2', holder2)
            # and, if it's not a comma
        elif(k2+1==len(no_journal_minus_starting_curly_bracket)):
            holder2+=v2[0]




        # if(v2[0]==','):
            # add space if there is another word
            # holder2+=v2[0]+ ' '
        # unless there is a comma in which case no space
        # else:
            # holder2+=v2[0]
    else:
        # no space if last element
        holder2+=v2[0]

print('line 77 (post last for-if, which assembles holder2) holder2: ', holder2 )

# print('line 79 (post last for-loop-if-else-combination, which assembles holder2) holder2[0]: ', holder2[0] )

