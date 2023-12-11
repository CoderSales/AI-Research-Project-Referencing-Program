# import numpy
# import pandas
# import openpyxl
from openpyxl import Workbook
import datetime
import os
import shutil
import os.path

# import parser1

import re

import importlib

# importlib.reload(parser)

# del parser

# import argparse
# import sys
# os_path_basename = os.path.basename(sys.argv[0])
# print(os_path_basename)
# argparse.ArgumentParser()

from importlib.metadata import version  

print(importlib.metadata)

# import parser
# importlib.reload(parser)


# parser1.parse()

your_path = os.environ.get("PWD")
root = your_path
files = [(path,f) for path,_,file_list in os.walk(root) for f in file_list]
f_name="Bibtex.bib"
from shutil import  copy
f = open(os.path.join(your_path, f_name), 'r', encoding="utf8")
for i in f.readlines():
    print(i)
f.close()

# for x in file:
#     for y in x:
#         if (/^journal/):
