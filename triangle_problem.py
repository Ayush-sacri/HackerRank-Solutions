import cmath
import math
from operator import length_hint

from numpy import char

length_ab=int(input("enter the value of ab "))
length_bc=int(input("enter the value of bc "))
length_ac=math.sqrt((length_ab**2)+(length_bc**2))
tangent=math.degrees(math.atan2(length_ab,length_bc))
#degree_sign = u"\N{Degree Sign}"
abcd=tangent
a=round(tangent)
if abcd-a>=0.5:
    a=a+1
    b=chr(176)
    print(f'{a}{b}')
else:
    b=chr(176)
    print(f'{a}{b}')
    
