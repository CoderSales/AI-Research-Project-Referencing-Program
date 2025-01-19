def year():
    """
    encapsulate author program in a
    function
    """
    # imports

    import nltk
    import re

    # file

    f_name="BibTex.bib"

    def opener(f_name):
        file = open(f_name, 'r', encoding="utf8")
        return file

    file=opener(f_name)

    # end prep

    endline=''
    file = opener(f_name)
    for line in file:
        if (re.search('^year',line)):
            starter=line
            line=line.lstrip('year = {')
            line=line.rstrip('},\n')

            endline=line
    # print(endline)
    return endline
