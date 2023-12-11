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
            print("on line 38 is: line[0] :", line[0])
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
print("line 55 (pre last for-loop-if-else-combination) : no_journal_minus_starting_curly_bracket :", no_journal_minus_starting_curly_bracket)

for k2,v2 in enumerate(no_journal_minus_starting_curly_bracket):
    # if (v2[0]):
    if (k2!=len(no_journal_minus_starting_curly_bracket)):
        # temporary test:
        typev2 = type(v2)
        print('typev2 =', typev2)
        print('v2 =', v2)
        print('v2[0] :',v2[0])
        typev2at0=type(v2[0])
        print('typev2at0 :',typev2at0)
        # add space if there is another word
        holder2+=v2[0]+ ' '
    else:
        # no space if last element
        holder2+=v2[0]

print('line 73 (post last for-loop-if-else-combination, which assembles holder2) holder2: ', holder2 )

# print('line 75 (post last for-loop-if-else-combination, which assembles holder2) holder2[0]: ', holder2[0] )

