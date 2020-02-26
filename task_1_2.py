import math 
x = float(input())
y = float(input())
result = (math.fabs(x) - math.fabs(y))/(1 + math.fabs(x*y))
print(result)