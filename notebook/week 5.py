# ============================================
# PRACTICE QUESTIONS + SOLUTIONS IN ONE FILE
# ============================================


# -----------------------------
# QUESTION 1 (LISTS)
# Create a list of 5 numbers, add a new number, 
# remove one number, and print the final list.
# -----------------------------
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.remove(20)
print("Q1 Final List:", numbers)



# -----------------------------
# QUESTION 2 (LISTS)
# Given a list: [9,8,2,3]
# Sort it in ascending order.
# -----------------------------
lst = [9, 8, 2, 3]
lst.sort(reverse=False)
print("Q2 Sorted List:", lst)



# -----------------------------
# QUESTION 3 (TUPLES)
# Create a tuple of 4 fruits and print the 2nd fruit.
# -----------------------------
fruits = ("apple", "banana", "mango", "orange")
print("Q3 Second Fruit:", fruits[1])



# -----------------------------
# QUESTION 4 (TUPLES)
# Convert a tuple into a list and add a new item.
# -----------------------------
t = (1, 2, 3)
t_list = list(t)
t_list.append(4)
print("Q4 Updated List:", t_list)



# -----------------------------
# QUESTION 5 (SETS)
# Create two sets and print their union and intersection.
# -----------------------------
a = {1, 2, 3}
b = {3, 4, 5}

print("Q5 Union:", a | b)
print("Q5 Intersection:", a & b)



# -----------------------------
# QUESTION 6 (SETS)
# Remove an element from a set if it exists.
# -----------------------------
s = {10, 20, 30}
s.discard(20)
print("Q6 After Discard:", s)



# -----------------------------
# QUESTION 7 (DICTIONARIES)
# Create a dictionary of student marks and print only the keys.
# -----------------------------
marks = {"Ram": 85, "Sita": 92, "Hari": 78}
print("Q7 Keys:", marks.keys())



# -----------------------------
# QUESTION 8 (DICTIONARIES)
# Add a new key-value pair and update an existing one.
# -----------------------------
student = {"name": "Supran", "age": 18}
student["college"] = "Beckett"
student["age"] = 19
print("Q8 Updated Dict:", student)



# -----------------------------
# QUESTION 9 (MIX)
# Store 3 students in a list of dictionaries.
# Print their names using a loop.
# -----------------------------
students = [
    {"name": "Supran", "age": 20},
    {"name": "Suridh", "age": 21},
    {"name": "Bizon", "age": 19}
]

print("Q9 Student Names:")
for st in students:
    print(st["name"])



# -----------------------------
# QUESTION 10 (MIX)
# Create a dictionary of emojis and replace words in a sentence.
# -----------------------------
sentence = "I am happy :) but sometimes sad :("
emoji_dict = {
    ":)": "😀",
    ":(": "☹️"
}

words = sentence.split(" ")
output = ''
for word in words:
    output += emoji_dict.get(word,word) + ' '
print("Q10 Emoji Output:", output)
