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

# your_path = os.environ.get("file")
# print(your_path)

# root = 'C:\\Users\\<username>\\OneDrive\\Documents\\<etc>' #  update this path
# your_path = 'C:\\Users\\<username>\\OneDrive\\Documents\\<etc>' #  update this path

# your_path = 'C:\\Users\\<username>\\OneDrive\\Documents\\<etc>' #  update this path

# root = 'C:\\Users\\<username>\\OneDrive\\Documents\\<etc>'


# print environment variables
# for var in os.environ:
#     print(var)



print(os.environ.get("PWD"))



your_path = os.environ.get("PWD")
# directory = string.replace(os.environ.get("PWD"), "/", "\\")

root = your_path
files = [(path,f) for path,_,file_list in os.walk(root) for f in file_list]

import shutil
import os.path


# print(files)

print(your_path)

f_name="Bibtex.bib"
from shutil import  copy
# f = open(r'C:\\Users\\<username>\\OneDrive\\Documents\\<etc>', 'r', encoding="utf8")

# f = open(your_path, 'r', encoding="utf8")
# f = open(your_path, 'rb', encoding="utf8")

f = open(os.path.join(your_path, f_name), 'r', encoding="utf8")
for i in f.readlines():
    print(i)
    # copy(i.strip(),r"E:\Images")    

f.close()




# while os.path.isdir (your_path):
#     # shutil.rmtree (your_path, ignore_errors=True)
#     with open('BibTex.bib','wb') as output:
#         for path, f_name in files:
#             with open(os.path.join(path, f_name), 'rb') as input:
#                 shutil.copyfileobj(input, output)
#             output.write(b'\n') # insert extra newline between files


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
