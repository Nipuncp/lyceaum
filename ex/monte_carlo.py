import random
import math
def monte_carlo(n):
    inside_circle = 0
    total = n
    while n > 1:
        x = random.random()
       # print(x)                
        y = random.random()
        #print(y)
        n -= 1
        if ((x**2 + y**2) <= 1):
         #   print(x**2 + y**2)
            inside_circle += 1
          #  print (inside_circle)
    print (n)
    pi = (inside_circle/total)*4
    return pi
