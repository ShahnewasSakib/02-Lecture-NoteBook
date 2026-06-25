# help funtion

help(len)

# strings

cat_name="luna"
age = 2
print(f"{cat_name} is {age} years old")

# split function

about = "This is for Missing Semester"
print(about.split())

# slicing

name = "Shahnewas"
print(name[::-1]) #reverse


# lists

lists=[2,3,4,5]
print(lists)

lists.append(6)
print(lists)
lists.append(6)
print(lists)
lists.append("Sakib")
lists.append(2.5)
print(lists)
# lists.remove("Sakib")
# print(lists)

# lists.sort() #sorting will not work when there are multiple types of data in the same list
print(lists)

days = ["Sat", "Sun", "Fri"]
for weekend in days:
    print(f"Today is {weekend}")
for num in range (0,10):
    print(num)

#dictionaries

cat = {
    "name": "Milo",
    "age": 2,
    "vaccinated": True
}

cat["Playful"] = "Yes"

for key,value in cat.items():
    print(key, value)

#object multiplication

matrix = [0]*3
print(matrix)

matrix = [[0]*3]
print(matrix)

matrix = [[0]*3]*3 #actually it's not a 3x3 matrix. all the 3 lists [0,0,0] are same
print(matrix)

matrix[0][0] = 1 #proof
print(matrix)

matrix = [[0]*3 for _ in range(3)] #the loop is running 3 times and creating 3 different [0]*3 lists
print(matrix)

matrix[0][0] =1
print(matrix)