def check_regex(regex, text):
    if regex == "" or regex == text:                # baseZERO case True
        return True
    if text == "":
        return False
        
    if regex[0] == "^":
        
        if regex[-1] == "$":
            if len(regex) == len(text) + 2:
                return match_string(regex[1:-1], text[-(len(regex)-1):])
            else:
                return False
        
        return match_string(regex[1:], text)        
        
    if regex[-1] == "$":
        return match_string(regex[:-1], text[-(len(regex)-1):])
        
    for i in range(len(text)):
        if match_string(regex, text[i:]):
            return True
    return False
        
    
def match_string(mregex, mtext):
    
    if mregex == "" or mregex == mtext:
        return True
    
    if mtext == "":
        return False
    
    if mregex[0] in mtext[0] + ".":
        return match_string(mregex[1:], mtext[1:])
        
    return False


regex, text = input().split("|")
print(check_regex(regex, text))
