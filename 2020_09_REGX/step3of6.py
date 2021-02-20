# write your code here
def match_string(regex, text):
    if regex == "" or regex == text:                #  option 1 - regex is True
        return True
    if text == "":
        return False                                #  option 2 - all text checked - no regex
    if regex[:1] in text[:1] + ".":                 #  option 3 - has to be investiated more
        return match_string(regex[1:], text[1:])
    return match_string(regex, text[1:])            #  option 4 - NEW check for shiifted text position

regex, text = input().split("|")
print(match_string(regex, text))
