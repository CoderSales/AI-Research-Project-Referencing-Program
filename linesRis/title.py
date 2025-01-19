def title():
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
        if (re.search('^title',line)):
            starter=line
            line=line.lstrip('title = {')
            line=line.rstrip('},\n')

            line=line.rstrip(' ')
            line=line.rstrip('},')


            endline=line
    # print(endline)
    return endline
