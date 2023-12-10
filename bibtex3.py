import numpy
import pandas
import openpyxl
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
import datetime
import os

print(os.environ.get("PWD"))


your_path = os.environ.get("PWD")

root = your_path

files = [(path,f) for path,_,file_list in os.walk(root) for f in file_list]

import shutil
import os.path

print(your_path)

f_name="Bibtex.bib"
from shutil import  copy

f = open(os.path.join(your_path, f_name), 'r', encoding="utf8")
for i in f.readlines():
    print(i)

f.close()
