def rt(reg,tex):
  print(reg," - ", tex)
  if reg == "":
    return True
  if tex == "":
    return False
  if reg[0] in tex[0] + ".":
    return rt(reg[1:], tex[1:])
  return False


rreg,ttex = input().split("|")

while ttex:                  #  Iterate on text_to_check
  if rreg[-1] == "$":        #  For precise end...
    ttex = ttex[-len(rreg.strip("$")):]   #  ...match legth of text_to_check
  if rt(rreg.strip("^$"),ttex):  #  MAIN TESTING CALL rt()
    break                    #  If regex correct do END (True)
  if rreg[0] == "^":         #  For precise start...
    ttex = []                #  ... if rt() returns False do END (False) 
  ttex = ttex[1:]            #  Calling back to "while" loop
                             #  If loop ends without rt() returning True...
                             #  ...send empty text_to_check (bool(""))
print(bool(ttex))
