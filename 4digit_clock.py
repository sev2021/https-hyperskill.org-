# BUILD LATEST POSSIBLE TIME USING FOUR RANDOM DIGITS
# (DONT FORGET FIRST TO VERIFY IF POSSIBLE)

def dtimer(four):                          # must be string, digits starting with zero issue
  sf = sorted([int(i) for i in four])      # sf is sorted list of input digits

  # verify if correct time can be made using 4 digits from input
  if (sf[0] in [0,1] and sf[1] < 6) or (sf[0] == 2 and sf[1] < 4 and sf[2] < 6):
  
    # result may start with digit 2 even if 2 is not the smallest digit -  example: 0123 -> 23:10
    if 2 in sf and len([i for i in sf if i < 6]) > 2:    
      stime = [2]                  # stime is final result, gets 2 as first digit here
      sf.remove(2)                 # remove digit from sf after added to stime
      t1 = max([i for i in sf if i < 4])
      sf.remove(t1)                 # remove digit from sf after added to stime
      t2 = max([i for i in sf if i < 6])
      sf.remove(t2)                 # remove digit from sf after added to stime
      stime = stime + [t1] + [t2] + sf
      print(stime, " TWO GOOD!")

    else:
      stime = [(0,1)[1 in sf[:2]]]   # stime is final result, gets first digt here
      sf.remove(stime[0])            # remove digit from sf after added to stime
      stime += [max(sf)]
      sf.remove(stime[1])            # remove digit from sf after added to stime
      stime = stime + [min(sf)] + [max(sf)]
      print(stime, " ONE/ZERO GOOD!")

  else:
    print("IMPOSSIBLE")
