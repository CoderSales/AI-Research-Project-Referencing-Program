

import lines

from lines import author

author=author.author()

# ___________________________________
def andReplacer():
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
        # if (re.search(' and ',line)):
            starter=line
            line=line.lstrip('author = {')
            line=line.rstrip('},\n')

            # line=line.lstrip(' and ')
            # line=line.rstrip('')

            # splitter = re.compile(r'(\sand+|\Sand')
            lineList=re.split(' and ', line)
            # print(line2)
            # splitter = re.compile(r' and ')
            # splitter.findall(line)
            # print(line)
            # print(splitter)
            
            # for x in lineList:
            #     lineList+=x
            # line=lineList
            
            # line=line.lstrip('[')
            # line=line.rstrip(']')

            line = re.sub(r', [][][^ ][azAZ] and ', ', ', line)
            # line = re.sub(r'[][^ ][azAZ] and ', ', ', line)
            line = re.sub(r' and ', ', ', line)
            endline=line

    # print(endline)

            

            # for x in lineList:
            #     print(x)
            #     lineList+=x
            # line2=lineList

    # return line2
    
    # return type(endline[:])
    return endline[:]


# andReplacer=andReplacer()
# print(andReplacer)
