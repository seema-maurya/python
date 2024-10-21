# List - ordered, mutable
marksOfStudents = [100, 200,100,150, 80]
print(marksOfStudents)


# updating values:
marksOfStudents[1] = 158
print(marksOfStudents)

# accessing elements
print(marksOfStudents[3])

# slicing:
print(marksOfStudents[:3])

#methods of list
# to check length:
length = len(marksOfStudents)
print(length)

#append:
marksOfStudents.append(150)
print(marksOfStudents)

#insert:
marksOfStudents.insert(0,120)
print(marksOfStudents)

#remove:
marksOfStudents.remove(80)
print(marksOfStudents)

# delete using index:
marksOfStudents.pop(4)
print(marksOfStudents)

#count:
total = marksOfStudents.count(100)
print(total)

#checking index of a values:
print(marksOfStudents.index(120))
print(marksOfStudents.index(100))

#sort & reverse:
marksOfStudents.sort()
print(marksOfStudents)

marksOfStudents.reverse()
print(marksOfStudents)

#copy:
marksOfStudents.copy()
print(marksOfStudents)

# For loops:
for i in marksOfStudents:
    print(i)


# types of list:
# int, string, float, boolean,mixed
#for example:
li1 = ["seema", "umaima", "nikita"]
li2 = [12.3, 45.6]
li3 = [true, false, true, false]
li4 = [1, "John",false,12.8,'c']


