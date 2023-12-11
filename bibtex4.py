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
from shutil import  copy
# f = open(os.path.join(your_path, f_name), 'r', encoding="utf8")
# for i in f.readlines():
#     print(i)
# f.close()

file = open("Bibtex.bib", 'r', encoding="utf8")

for x in file:
    # if ('journal' in x):
    # if (x.startswith('journal')):
    if (re.search('^journal',x)):
        tokens = nltk.word_tokenize(x)
        # print(tokens)

        tagged = nltk.pos_tag(tokens)

        remove_end = tagged[0:-1]
        # print(remove_end)
        # print(type(remove_end))
        
        for x in remove_end:
            print(x[0])
            x[0]
        # print(x,sep='')


#     for y in x:
#         if (/^journal/):
