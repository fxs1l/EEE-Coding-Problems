#These imports are necessary. No need to modify the import statements.
from operator import truediv, mul, add
from math import sqrt

def quad(a,b,c):
  ### Insert Code Below (15 lines are below. Use them all for full credit. White space and comments are not included.) 
 return int(truediv(add(mul(-1,b),sqrt(add(mul(b,b),mul(-1,mul(4,mul(a,c)))))),mul(2,a)))

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  ###

#This is a way of assigning three comma separated inputs into three int variables. It would be advisable to look into the input(), split(), and int() functions. No need to modify the two lines below.
in1, in2, in3 = input().split(",")
in1, in2, in3 = int(in1), int(in2), int(in3)

###Call the function and print the result below.
print(quad(in1,in2,in3))

###End
