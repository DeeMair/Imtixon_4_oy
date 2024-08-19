"""3.Masala"""

students = []
with open("students.txt", "r") as file:
    students = file.readlines()

file = open("famila.txt", "w")
for i in students:
    name, ball = i.split(", ")
    familya, ism = name.split()
    file.write(f"{familya[0]}.{ism}, {ball}")

