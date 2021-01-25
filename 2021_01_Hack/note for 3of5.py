######   for step 3 of 5 - getting all lowcase / upcase combination for string
######   defauls string all lowcase is_pass
######   Using external module itertools

import itertools

is_pass = "abcde"
print("Test word:",is_pass)


for k in list(itertools.product([0,1],repeat=len(is_pass))):  #  iterate possible 1-0
    print(*[(ch,ch.upper())[k[i]] for i,ch in enumerate(is_pass)])  #  translate 1-0 to low-up case
