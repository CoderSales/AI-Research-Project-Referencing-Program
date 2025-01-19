def risL1():
    """
    encapsulate ris L1 (link other than url) program in a
    function
    """
    # imports

    import nltk
    import re

    # file

    f_name="BibTex.ris"

    def opener(f_name):
        file = open(f_name, 'r', encoding="utf8")
        return file

    file=opener(f_name)

    # end prep

    endline=''
    file = opener(f_name)
    for line in file:
        if (re.search('^L1 - ',line)):
            starter=line
            line=line.lstrip('L1 - ')
            # line=line.rstrip('},\n')

            endline=line
    # print(endline)
    return endline
# author=risL1()
# print(risL1)