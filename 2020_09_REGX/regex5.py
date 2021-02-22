#  ################# FINAL ###################
#  ## EDIT 2021 - Gosh this code sucks ;)  ###
#  ## There is better way to solve it
#  ## See new files in this folder

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
      return rt(reg[2:], tex)    #### this may need refactoring, see "*"

    if reg[0] != reg[2]:           #  ?2 Is there one more same letter...
      return rt(reg[2:], tex[1:])   #  ...if not, use the lette
    else:
      if reg[0] == tex[1]:         #  ?3  If we need extra letter to match...
        return rt(reg[3:], tex[2:])  #  ...use both letter and extra letter
      else:                        #  ?4  If we dont need extra letter...
        return rt(reg[3:], tex[1:])  #  ...use only one letter

  if reg[1:].startswith("+"):
    if reg[0] not in tex[0] + ".":   #  if key letter is not text letter END-FAIL
      return False
    reg = tex[0] + reg[1:]          #  if key was "." it will be letter now
    regl = len(reg[2:]) - len(reg[2:].strip(reg[0]))  #  count number of keys in reg
    texl = len(tex) - len(tex.lstrip(tex[0]))  #  count number of keys in tex
    if texl < regl + 1:    #  If there is less keys in txt than reg(+1 from condit)...
      return False         #  ...then it is impossible to replace it with regex
    return rt(reg[(2 + regl):], tex.lstrip(tex[0]))

  if reg[1:].startswith("*"):
    if len(reg) == 2:
      return True            #  Any option will match END-SUCCESS    
    if reg[0] != reg[2] and reg[0] != ".":             #  *1 If key not replied after *...
      return rt(reg[2:], tex.lstrip(reg[0]))   #  ...remove all keys (if any) from tex
    if reg[0] != ".":
      regl = len(reg[2:]) - len(reg[2:].strip(reg[0]))  #  count number of keys in reg
      texl = len(tex) - len(tex.lstrip(tex[0]))  #  count number of keys in tex      
      if texl < regl:    #  If there is less keys in txt than reg...
        return False     #  ...then it is impossible to replace it with regex
      return rt(reg[(2 + regl):], tex.lstrip(tex[0]))

    # ###############  THIS PART IS FOR DOT .  AS A KEY   ###########
    if reg[2] != tex[0]:                #  Letter after key differ first letter of tex?
      if not tex.lstrip(tex[0]).startswith(reg[2]):  #  Letter after key differ next after above?
        return False                    #  Cant use letter after key END-FAIL
      else:
        return rt(reg[3:], tex.strip(tex[0])[1:])
    else:
      reg = reg[2] + reg[1:]    # If letter after key match first letter of tex..
      return rt(reg,tex)        # ...run loop again with dot replaced with that letter
    
  if reg[0] in tex[0] + ".":       # main rt() function call for next loop
    return rt(reg[1:], tex[1:])
  return False                     # main rt() function END-FALSE


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
