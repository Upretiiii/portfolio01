def multiply(a, b=None):
    if b is None:
        b = a
    return a * b

print("multiply(5, 3) =", multiply(5, 3)) 
print("multiply(4) =", multiply(4))       
print("multiply(7, 2) =", multiply(7, 2))  
print("multiply(9) =", multiply(9))        

def someFunc(x, y, z):
    print("x is", x)
    print("y is", y)
    print("z is", z)

someFunc(y=2, z=3, x=1)
someFunc(z=99, y=4, x=10)
someFunc(5, z=7, y=6)  

def showMsg(title, body="", prefix="INFO", suffix="."):
    print(prefix, title, body, suffix)


showMsg("File opened")
showMsg("File not opened", prefix="ERROR")
showMsg("File missing", body="Insert Disk", suffix="Press return")

print("Apple", "Banana", "Cherry", sep=", ")
print("2025", "12", "10", sep="-")
print("A", "B", "C", sep=" | ")

def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

print("Average of 4, 5, 6 =", calcAve(4, 5, 6))
print("Average of 10, 20 =", calcAve(10, 20))
print("Average of 1, 2, 3, 4, 5 =", calcAve(1, 2, 3, 4, 5))
