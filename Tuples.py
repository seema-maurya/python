# 1. Write a Python program to find the number of times 4 appears in the tuple.
#Input
# Given tuple
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)

# Count occurrences of 4
count_of_fours = tuplex.count(4)

# Output the result
print(count_of_fours)


# 2.Write a Python program to convert a list to a tuple.
# Given list
listx = [5, 10, 7, 4, 15, 3]

# Convert list to tuple
tuplex = tuple(listx)

# Output the result
print(tuplex)


#3. Write a Python program to calculate the sum of the numbers in a given tuple.
# Given list of tuples
tuples_list = [(1, 2), (3, 4), (5, 6)]

# Calculate the sum of the numbers in the tuples
total_sum = sum(sum(tup) for tup in tuples_list)

# Output the result
print(total_sum)


#4.Write a python program and iterate the given tuples
#Input:
# Given tuples
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# List of employees
employees = [employee1, employee2, employee3]

# Iterate through the tuples and print details
for employee in employees:
    name, emp_id, department, salary = employee
    print(f"Name: {name}, ID: {emp_id}, Department: {department}, Salary: ${salary}")



#outputs:
========= RESTART: /Users/ashishmaurya/Desktop/Anudip/python/Tuples.py =========
3
(5, 10, 7, 4, 15, 3)
21
Name: John Doe, ID: 101, Department: Human Resources, Salary: $60000
Name: Alice Smith, ID: 102, Department: Marketing, Salary: $55000
Name: Bob Johnson, ID: 103, Department: Engineering, Salary: $75000
