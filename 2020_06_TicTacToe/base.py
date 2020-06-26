# Tic Tac Toe game

st = "OOOOXOX_O"
sr = [st[0:3], st[3:6], st[6:9], st[0:7:3], st[1:8:3], st[2:9:3], st[0:9:4], st[2:7:2]]

def s_print(string):
  print(string[0:3])
  print(string[3:6])
  print(string[6:9])

def s_win(result, string):
  if("OOO" in result and "XXX" in result 
    or abs(string.count("O") - string.count("X")) > 1):

    print("Impossible")
  elif "OOO" in result:
    print("O wins")
  elif "XXX" in result:
    print("X wins")
  else:
    print("No winner")

s_print(st)
s_win(sr, st)

# === debugging only ===
print("==============")
print(st)
print("==============")
print(sr)
