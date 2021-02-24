
def match_string(mregex, mtext, regex, bslash):
    
    if mregex[0:1] == "\\":  
        return match_string(mregex[1:], mtext, regex, 1)

    if mregex == mtext:
        return True

    if mregex == "":
        if mtext != "" and regex[-1:] == "$" and regex[-2:-1] != "\\":
            return False
        return True

    if mtext == "":
        return False
    
    if mregex[1:2] == "?" and bslash == 0:
        return match_string(mregex[2:], mtext, regex, 0) or match_string(mregex[0] + mregex[2:], mtext, regex, 0)
        
    if mregex[1:2] == "*" and bslash == 0:
        for i in range(len(mtext)):
            if match_string(mregex[0] * i + mregex[2:], mtext, regex, 0):
                return True
        if match_string(mregex[2:], mtext, regex, 0):
            return True
        return False
        
    if mregex[1:2] == "+" and bslash == 0:
        for i in range(1, len(mtext)):
            if match_string(mregex[0] * i + mregex[2:], mtext, regex, 0):
                return True
        return False
    
    if mregex[0] == mtext[0] or mregex[0] == "." and bslash == 0 or mregex[0] == "." and mtext[0] == "." and bslash == 1:
        return match_string(mregex[1:], mtext[1:], regex, 0)
    
    return False


regex, text = input().split("|")
result = False

clean_regex = regex
if clean_regex[:1] == "^":
    clean_regex = clean_regex[1:]
if clean_regex[-1:] == "$" and clean_regex[-2:-1] != "\\":
    clean_regex = clean_regex[:-1]

for i in range(len(text) + 1):

    if match_string(clean_regex, text[i:], regex, 0):
        if regex[:1] == "^" and i > 0:
            break
        result = True
        break
        
print(result)
