# write your code here
def match_string(regex, text):
    if regex == "" or regex == text:                #  option 1 - regex is True
        return True       
    if regex[:1] in text[:1] + ".":                 #  option 2 - has to be investiated more 
        return match_string(regex[1:], text[1:])    
    return False                                    #  option 3 - regex doesnt work

regex, text = input().split("|")
print(match_string(regex, text))
