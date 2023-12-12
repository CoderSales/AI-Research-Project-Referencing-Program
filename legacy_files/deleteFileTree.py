"""

WARNING!!!! 

REMOVES ALL FILES IN TREE 

STARTING FROM 

ROOT LOCATION

SPECIFIED IN

your_path

IRREVERSIBLE ACTION!!!!

NO SAFETY CHECK

RUNS IMMEDIATELY!!!

"""

import numpy
import pandas
import openpyxl
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
import datetime

import os


import shutil

your_path = 'C:\\Users\\<user>\\OneDrive\\Documents\\<etc>' # edit

while os.path.isdir (your_path):
    shutil.rmtree (your_path, ignore_errors=True)
os.makedirs (your_path)


# new code:

import shutil
import os.path

your_path=os.getcwd()
print(your_path)
while os.path.isdir (your_path):
    shutil.rmtree (your_path, ignore_errors=True)
os.makedirs (your_path)
