def check_regex(regex, text):
    
    if regex == "" or regex == text:                # baseZERO case True
        return True
    
    if text == "":
        return False
                
    for i in range(len(text) + 1):
        if match_string(regex.strip("^$"), text[i:], regex):
            if "^" in regex and i > 0:
                return False
            return True
    return False
        
    
def match_string(mregex, mtext, regex):
    
    if mregex == mtext:
        return True
    
    if mtext == "":
        return False

    if mregex == "":
        if "$" in regex and mtext != "":
            return False
        return True
    
    if mregex[1:2] == "?":                            #  added in step 5
        return match_string(mregex[2:], mtext, regex) or match_string(mregex[0] + mregex[2:], mtext, regex)
        
    if mregex[1:2] == "*":
        for i in range(len(mtext)):                  #  added in step 5
            if match_string(mregex[0] * i + mregex[2:], mtext, regex):
                return True
        if match_string(mregex[2:], mtext, regex):
            return True
        return False
        
    if mregex[1:2] == "+":                           #  added in step 5
        for i in range(1, len(mtext)):
            if match_string(mregex[0] * i + mregex[2:], mtext, regex):
                return True
        return False
    
    if mregex[0] in mtext[0] + ".":  
        return match_string(mregex[1:], mtext[1:], regex)
        
    return False


regex, text = input().split("|")
print(check_regex(regex, text))
