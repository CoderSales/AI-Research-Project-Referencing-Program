import numpy
import pandas
import openpyxl
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
import datetime

# wb.save("sample.xlsx") # to end

ref=open('BibTex.bib', 'r', encoding='utf-8')
for line in ref:
    print('hi')
