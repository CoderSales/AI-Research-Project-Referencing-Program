# imports

import nltk
import re

# file

f_name="Bibtex.bib"
file = open("Bibtex.bib", 'r', encoding="utf8")

# end prep

holder=""
count=1
lines=1
file1=file
for line1 in file1:
    lines=lines+1
    
print(lines, "lines in BibTex.bib")

endline=''
file = open("Bibtex.bib", 'r', encoding="utf8")
for line in file:
    # print(count)
    # count=count+1
    if (re.search('^journal',line)):
        starter=line
        line=line.lstrip('journal = {')
        line=line.rstrip('},\n')
        # print(starter)
        # print(line)
        endline=line
print(endline)
# print(count)
# len_journal=len('journal={')
# for line in file:
#     if (re.search('^journal',line)):
#         tokens = nltk.word_tokenize(line)
#         tagged = nltk.pos_tag(tokens)
#         remove_end = tagged[0:-2] # cut space and last curly bracket
#         for k,tuple_key_word in enumerate(remove_end, start = 0):
#             if(tuple_key_word[0]!=len(remove_end)): # remove_end may be line instead
#                 holder+=tuple_key_word[0]+' '
#             else:
#                 holder+=tuple_key_word[0]
#             if(re.search('^journal',holder)):
#                 start_after_journal=slice(len_journal,None,1)
#                 no_journal=holder[start_after_journal]
# tokens_no_journal = nltk.word_tokenize(no_journal)
# tagged_tokens_no_journal = nltk.pos_tag(tokens_no_journal)
# no_journal_minus_starting_curly_bracket = tagged_tokens_no_journal[1:] # cut space and last curly bracket
# holder2=''
# list_of_keys=[]
# for k3,v3 in no_journal_minus_starting_curly_bracket:
#     list_of_keys.append(k3)
# print(list_of_keys)
# for k2,v2 in enumerate(list_of_keys):
#     if (k2!=len(list_of_keys)):
#         if (k2+1!=len(list_of_keys)): # avoids index out of range error
#             print('line 35:',list_of_keys[k2+1])
#             if(v2 != ',' and list_of_keys[k2+1]==','): # if this isn't but next element is a comma:
#                 print('\n', 'line 37: start of 1 off block for comma next',sep="")
#                 print('line 38: (k2) :',k2)
#                 print('line 39: (v2), list_of_keys[k2+1]:',v2, list_of_keys[k2+1])
#                 print('line 40: so, list_of_keys[k2+1] = ', list_of_keys[k2+1])
#                 holder2 += v2 # wait, save space for next element coming in.
#                 print('line 42: holder2',holder2)
#                 print('line 43: end of 1 off block for comma next', '\n')
#             elif(v2 != ',' and list_of_keys[k2+1]!=','): # if this element is not a comma, and neither is next:
#                 holder2 += v2 + ' ' # then can add a space
#                 print('line 46: holder2', holder2)
#         elif(k2+1 == len(list_of_keys)):
#             holder2 += v2 # experience
#     else:
#         # no space if last element
#         holder2+=v2[0]
# print('line 52: (post last for-if, which assembles holder2) holder2:', holder2 )
