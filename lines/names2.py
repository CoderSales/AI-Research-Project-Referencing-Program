def names2():
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
        if (re.search('^author',line)):
            starter=line
            # print(starter)
            line=line.lstrip('author = {')
            line=line.lstrip(', ')
            re.search('author = {',line)
            line=line.rstrip('},\n')

            endline=line
    # print(endline)
    return endline
# names2=names2()
# print(names2)
