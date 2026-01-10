# Continue:

grades = [20, 50, 43, 33, 90, 15]
pass_mark = 40
passes = 0
total_passes = 0
for grade in grades:
    if grade < pass_mark:
        continue
    passes += 1
    total_passes += grade
print("Average pass mark was:", total_passes / passes)


# Break:

numbers = [10, 20, 30, 90, 200, 30, 22, 11]
total = 0
for num in numbers:
    if num > 100:
        print("Number over 100 found, breaking loop!")
        break
    total += num
    print("Running total:", total)
else:
    print("All numbers processed")
