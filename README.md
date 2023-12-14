# AI-Research-Project-Referencing-Program

## Description

AI-Research-Project-Referencing-Program-Attempt

## Recommended Requirements (setup tested for)

Windows

Visual Studio Code

wsl

wsl2

git bash

## To Run

clone or download repository

from root directory run

python -m venv .venv2

source .venv2/Scripts/activate

pip install -r requirements.txt

python main.py

### to edit

replace BibTex.bib

with a BibTex.bib

downloaded from the journal article to be referenced

run above command

## Table of Contents

Documentation

- [01st20docs](https://github.com/CoderSales/AI-Research-Project-Referencing-Program/tree/main/documentation/01st20docs)

    - has [20DEVELOPMENT.md](https://github.com/CoderSales/AI-Research-Project-Referencing-Program/blob/main/documentation/01st20docs/20DEVELOPMENT.md)

        - describes prior state of development of project

- [02nd20docs](https://github.com/CoderSales/AI-Research-Project-Referencing-Program/tree/main/documentation/02nd20docs)

    - has [21OldREADME.md](https://github.com/CoderSales/AI-Research-Project-Referencing-Program/blob/main/documentation/02nd20docs/21OldREADME.md)

        - includes:
        
        - RegEx Quickguide

        - imports openpyxl, NLTK

        - References

    - has [22DEVELOPMENT.md](https://github.com/CoderSales/AI-Research-Project-Referencing-Program/blob/main/documentation/02nd20docs/22DEVELOPMENT.md)

        - describes **current** state of development of project

        - supercedes 01st20docs/20DEVELOPMENT.md

## Content

### Summary and Current Status

```text
TODO: (In Progress) Make an automatic referencing program.

- Input: Take BibTex.bib

- Output: Reference

- How it works:
  - main.py calls a couple python files in the root directory like date.py
    and imports folders files and functions from lines folder
    - one file either author.py or journal.py
      was used to develop functionality
      of going through a line of the BibTex.bib
      file
      searching for a starting element
      stripping this
      and returning the relevant substring
      then this was copied and edited
      to add different functionality for the
      various parts of the reference 
      main assembles these
      and prints reference
      

- Next step : Trying to replace author first name with
  initial and dot in author string
  from author line
  from
  file
  BibTex.bib  
```

## References

