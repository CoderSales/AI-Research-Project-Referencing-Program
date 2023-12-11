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
        for line in remove_end:
            if(x[position]!=length(whatever_passed_in_string)):
                holder+=line[0]+' '
            else:
                holder+=line[0]
            if(re.search('^journal',holder)):
                start_after_journal=slice(len_journal,None,1)
                no_journal=holder[start_after_journal]


print(no_journal)
