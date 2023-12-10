import numpy
import pandas
import openpyxl
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
import datetime


# new code: Question:

import os

# print environment variables
# for var in os.environ:
#     print(var)



print(os.environ.get("PWD"))



your_path = os.environ.get("PWD")

root = your_path
files = [(path,f) for path,_,file_list in os.walk(root) for f in file_list]

import shutil
import os.path


# print(files)

print(your_path)

f_name="Bibtex.bib"
from shutil import  copy

f = open(os.path.join(your_path, f_name), 'r', encoding="utf8")
for i in f.readlines():
    print(i)

f.close()




# with open('BibTex.bib','wb') as output:
#     for path, f_name in files:
#         with open(os.path.join(path, f_name), 'rb') as input:
#             shutil.copyfileobj(input, output)
#         output.write(b'\n') # insert extra newline between files


# os.makedirs (your_path)


# # new code:

# import shutil
# import os.path

# # with open('BibTex.bib','wb') as output:
# #     for path, f_name in files:
# #         with open(os.path.join(path, f_name), 'rb') as input:
# #             shutil.copyfileobj(input, output)
# #         output.write(b'\n') # insert extra newline between files





# # old code:

# # bibtex_str = open('BibTex.bib', 'r')
# # # ref=open('BibTex.bib', 'r')
# # for line in bibtex_str:
# #     print(hi)

# # import bibtexparser
# # library = bibtexparser.parse_string(bibtex_str) # or bibtexparser.parse_file("my_file.bib")
