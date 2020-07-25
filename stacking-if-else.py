# HOW TO STACK if-else expressions:
# classic construction:

def ii(x):
  if x < 0:
    print("minus")
  else:
    if x > 0:
      print("plus")
    else:
      print("zero")

# PYTHON(C) one-liner ;)

def jj(x):
  print("minus" if x < 0 else "plus" if x > 0 else "zero")
