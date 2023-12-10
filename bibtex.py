import numpy
import pandas
import openpyxl
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
import datetime


# bibtex_str = """
# @comment{
#     This is my example comment.
# }

# @ARTICLE{Cesar2013,
#   author = {Jean César},
#   title = {An amazing title},
#   year = {2013},
#   volume = {12},
#   pages = {12--23},
#   journal = {Nice Journal}
# }
# """


# new code: Question:

import os
root = 'C:\\Users\\<username>\\OneDrive\\Documents\\<etc>' #  update this path
files = [(path,f) for path,_,file_list in os.walk(root) for f in file_list]

import shutil

while os.path.isdir (your_path):
    shutil.rmtree (your_path, ignore_errors=True)
os.makedirs (your_path)


# new code:

import shutil
import os.path

with open('BibTex.bib','wb') as output:
    for path, f_name in files:
        with open(os.path.join(path, f_name), 'rb') as input:
            shutil.copyfileobj(input, output)
        output.write(b'\n') # insert extra newline between files





# old code:

# bibtex_str = open('BibTex.bib', 'r')
# # ref=open('BibTex.bib', 'r')
# for line in bibtex_str:
#     print(hi)

# import bibtexparser
# library = bibtexparser.parse_string(bibtex_str) # or bibtexparser.parse_file("my_file.bib")
