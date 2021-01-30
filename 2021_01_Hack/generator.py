##########  YIELD / generators
################################

##  1.generate iterable function

def fun(x):
  for i in x:
    yield x * 10
    
##  2.call function ITERABLE way

print(*fun(7))    ##  print with star (*) operator

list(fun(7))      ##  turn it into list




