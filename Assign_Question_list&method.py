#Updating values:
# Q1: How do you update the first value in a list of numbers?
numbers = [10, 20, 30, 40]
numbers[0] = 100
print(numbers)

#  How do you update the last element of a list?
numbers = [5, 10, 15, 20]
numbers[3] = 50
print(numbers)

#Q3: Change the second value of the list colors = ['red', 'blue', 'green'] to 'yellow'.
colors = ['red', 'blue', 'green']
colors[1] = 'yellow'
print(colors)

#Q4: How to update the value at index 3 of the list?
fruits = ['apple', 'banana', 'cherry', 'date']
fruits[3] = 'dragonfruit'
print(fruits)


# 2. Accessing elements:
# Q1: How do you access the first element of a list?
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])

#How do you access the last element in a list?
fruits = ['apple', 'banana', 'cherry']
print(fruits[2])

# Access the second element from the list animals = ['dog', 'cat', 'elephant']
animals = ['dog', 'cat', 'elephant']
print(animals[1])

#3. Slicing:
#Q1: Get the first 3 elements from the list.
numbers = [1, 2, 3, 4, 5]
print(numbers[:3])

#Slice the last 2 elements from the list.
numbers = [10, 20, 30, 40, 50]
print(numbers[-2:])

#  Slice from the second to fourth elements.
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[1:4])

#Methods of list:
# 1. Length:
# Q1: Find the length of a list of numbers.
numbers = [10, 20, 30, 40]
print(len(numbers))

# What is the length of the list animals = ['cat', 'dog', 'elephant']
animals = ['cat', 'dog', 'elephant']
print(len(animals))

# Find the length of an empty list.
empty_list = []
print(len(empty_list))

# 2. Append:
# Q1: How do you add a number to a list?
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

# Append 'orange' to the list of fruits.
fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)

# How do you add 100 to the list of numbers?
numbers = [10, 20, 30]
numbers.append(100)
print(numbers)

# 3. Insert:
#Q1: Insert 50 at index 1 in the list numbers.
numbers = [10, 20, 30]
numbers.insert(1, 50)
print(numbers)

# Insert 'grapes' at the second position in the list fruits
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'grapes')
print(fruits)

# 4. Remove:
# Q1: Remove 'apple' from the list.
fruits = ['apple', 'banana', 'cherry']
fruits.remove('apple')
print(fruits)

# remove 'blue' from the list?
colors = ['red', 'blue', 'green']
colors.remove('blue')
print(colors)

# Remove 30 from the list of numbers.
numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)

#5. Delete using index:
#Q1: Delete the first element from the list numbers.
numbers = [1, 2, 3, 4]
del numbers[0]
print(numbers)


#Delete the element at index 2 from colors = ['red', 'green', 'blue', 'yellow']
colors = ['red', 'green', 'blue', 'yellow']
del colors[2]
print(colors)

# Delete the element at index 1 from the list of numbers.
numbers = [10, 20, 30, 40]
del numbers[1]
print(numbers)

# 6. Count:
#Q1: Count how many times 'apple' appears in the list.
fruits = ['apple', 'banana', 'apple', 'cherry']
print(fruits.count('apple'))

# How many times does 20 appear in the list of numbers
numbers = [10, 20, 30, 20, 40]
print(numbers.count(20))

#Count how many times 'dog' is present in animals = ['cat', 'dog', 'dog', 'elephant']
animals = ['cat', 'dog', 'dog', 'elephant']
print(animals.count('dog'))

# 7. Sort & Reverse:
# Q1: How do you sort the list [5, 2, 9, 1] in ascending order
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)

# Sort the list ['apple', 'banana', 'cherry'] in reverse alphabetical order.
fruits = ['apple', 'banana', 'cherry']
fruits.sort(reverse=True)
print(fruits)

# How do you reverse the order of the list [10, 20, 30, 40]
numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)

# 8. Copy:
#How do you make a copy of the list [10, 20, 30]
numbers = [10, 20, 30]
copy_of_numbers = numbers.copy()
print(copy_of_numbers)


# 4. For Loops:
#Q1: How do you print each element of the list [1, 2, 3] using a for loop
numbers = [1, 2, 3]
for num in numbers:
    print(num)

# Use a for loop to print each fruit in the list ['apple', 'banana', 'cherry']
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Print all animals in the list ['dog', 'cat', 'rabbit'] using a for loop.
animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print(animal)





