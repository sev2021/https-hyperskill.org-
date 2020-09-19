def rt(reg,tex):
  print(reg," - ", tex)
  if reg == "":
    return True          #  True condition END-SUCCESS
  if tex == "":
    return False

  if reg[1:].startswith("?"):
    if len(reg) == 2:
      return True            #  Any option will match END-SUCCESS
    if reg[0] not in tex[0] + ".":   #  ?1  Dont use letter, it doesnt match
      return rt(reg[2:], tex)

    if reg[0] != reg[2]:           #  ?2 Is there one more same letter...
      return rt(reg[2:], tex[1:])   #  ...if not, use the lette
    else:
      if reg[0] == tex[1]:         #  ?3  If we need extra letter to match...
        return rt(reg[3:], tex[2:])  #  ...use both letter and extra letter
      else:                        #  ?4  If we dont need extra letter...
        return rt(reg[3:], tex[1:])  #  ...use only one letter

  if reg[1:].startswith("+"):
    if reg[0] not in tex[0] + ".":   #  if key letter is not text letter END-FALSE
      return False
    reg = tex[0] + reg[1:]          #  if key was "." it will be letter now
    regl = len(reg[2:]) - len(reg[2:].strip(reg[0]))  #  count number of keys in reg
    texl = len(tex) - len(tex.lstrip(tex[0]))  #  count number of keys in tex
    print(regl, " - ", texl)    ######### DEBUG PRINT ###########
    if texl < regl + 1:    #  If there is less keys in txt than reg(+1 from condit)...
      return False         #  ...them it is impossible to replace it with regex
    return rt(reg[(2 + regl):], tex.lstrip(tex[0]))

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
    ttex = []                #  ... if rt() returned False do END (False) 
  ttex = ttex[1:]            #  Calling back to "while" loop
                             #  If loop ends without rt() returning True...
                             #  ...send empty text_to_check (bool(""))
print(bool(ttex))
