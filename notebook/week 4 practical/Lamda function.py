import math

hypot = lambda a, b: math.sqrt(a * a + b * b)

print("hypot(3,4) =", hypot(3, 4)) 

print("Type of hypot variable:", type(hypot))  

to_seconds = lambda hours, minutes: hours * 3600 + minutes * 60

print("to_seconds(0,2) =", to_seconds(0, 2))    
print("to_seconds(2,0) =", to_seconds(2, 0))    
print("to_seconds(1,30) =", to_seconds(1, 30))  

to_seconds = lambda hours, minutes=0: hours * 3600 + minutes * 60

print("to_seconds(1) =", to_seconds(1))  
print("to_seconds(2) =", to_seconds(2))  
print("to_seconds(1,45) =", to_seconds(1, 45))  



