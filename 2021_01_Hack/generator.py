##########  YIELD / generators
################################

##  1.generate iterable function

def fun(x):
  for i in range(x):
    yield i * 10
    
##  2.call function ITERABLE way

print(*fun(7))    ##  print with star (*) operator

list(fun(7))      ##  turn it into list

## use next() to iterate 

ff = fun(10)
print(next(ff))    ##  returns 0
print(next(ff))    ##  returns 10
print(next(ff))    ##  returns 20
print(next(ff))    ##  etc...


