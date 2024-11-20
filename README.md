# AI-Research-Project-Referencing-Program

## Description

AI Research Project Referencing Program Attempt

Take in BibTex file

downloaded for a journal article to be referenced

Outputs formatted reference.

(Some manual post editting necessary, like italics 

and 

repllacing Author first names

with initials)

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

- nicetohave:
  - for D.R.Y.
    pass each lines identifier
    e.g. journal
    into a single file
    or function call as an argument
    and then
    use same function
    and send in the following:
    
```

```python

listOfIdentifiers=['author', 'journal', <etc.> ]

for identifier in listOfIdentifiers:
    listOfValues=[]
    returnValue=functionCall(identifier)
    listOfValues.append(returnValue)
listOfValues
```

```text
where functionCall
could be a single file
or 
possibly
a
function directly in main.py
called which handles
for each line of
BibTex.bib
returns the corresponding
value

then need to
format listOfValues
into
output of reference
(similar to how currently done
in main.py
albeit currently
using print statement(s))

Add
GitHub suggested
automated workflow
.github/workflows/python-app.yaml
tests deploys
python application
```

## Troubleshooting

If it's not working:

delete space to the left of key value pairs in BibTex.bib file

e.g.

```BibTex
@article{vaswani2023attentionneed,
      title={Attention Is All You Need}, 
      author={Ashish Vaswani and Noam Shazeer and Niki Parmar and Jakob Uszkoreit and Llion Jones and Aidan N. Gomez and Lukasz Kaiser and Illia Polosukhin},
      year={2023},
      eprint={1706.03762},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/1706.03762}, 
}
```

to this:

```BibTex
@article{vaswani2023attentionneed,
title={Attention Is All You Need}, 
author={Ashish Vaswani and Noam Shazeer and Niki Parmar and Jakob Uszkoreit and Llion Jones and Aidan N. Gomez and Lukasz Kaiser and Illia Polosukhin},
year={2023},
eprint={1706.03762},
archivePrefix={arXiv},
primaryClass={cs.CL},
url={https://arxiv.org/abs/1706.03762}, 
}
```

also try ensuring BibTex.bib starts with

```BibTex
@article
```

## References

see [documentation](https://github.com/CoderSales/AI-Research-Project-Referencing-Program/tree/main/documentation)
