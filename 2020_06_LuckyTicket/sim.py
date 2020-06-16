# try to make it primitive way ;)

def lucky-number():
  print("Enter 6-digit number: ")
  x = input()
  y = x//100000%10 + x//10000%10 + x//1000%10
  z = x//1000%10 + x//100%10 + x%10
  print("First three digits = ",y)
  print("Last three digits = ",z)
