import author

# delete:
author=author.author()
# print(author)

for name in author:
    print(name)

# for line in file:
#     if (re.search('^journal',line)):
#         tokens = nltk.word_tokenize(line)
#         tagged_list = nltk.pos_tag(tokens)

#         for k4, v4 in enumerate(tagged_list):
#             # k4 is number
#             # v4 is a unique tuple per iteration of line 16 for loop
#             for tagged_keys_for_use, _ in tagged_list: # splits out v4

#                 # tagged_keys_for_use

#                 # tagged_list = tagged

#                 # highlights x and x1 same, y and y1 not same:
#                 # x, y are tuples
#                 # x1, y1 are strings
#                 x = tagged_list[k4][0]
#                 x1 = tagged_keys_for_use
