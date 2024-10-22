# Q1: Create a list of city names, add 8 elements in it, and perform CRUD operations
# Create a list of city names (CRUD: Create)
cities = ["New York", "London", "Paris", "Tokyo", "Berlin", "Sydney", "Mumbai", "Toronto"]

# Read operation (Display the list)
print("Original List of Cities:", cities)

# Update operation (Changing the 2nd city to 'Los Angeles')
cities[1] = "Los Angeles"
print("After Update:", cities)

# Delete operation (Removing 'Berlin')
cities.remove("Berlin")
print("After Deleting 'Berlin':", cities)

# Add a new city (CRUD: Add)
cities.append("Singapore")
print("After Adding 'Singapore':", cities)


# Q2: Create a mixed list and change the value of the third index 
# Create a mixed list
mixed_list = [12, "Hello", 3.14, True, "World"]

# Changing the value at the 3rd index 
mixed_list[2] = 42
print("After Changing 3rd Index Value:", mixed_list)


# Q3: Create a list of country names, reverse the list, and print only middle elements
# Create a list of countries
countries = ["India", "USA", "Brazil", "Japan", "Germany", "Australia", "Canada", "France"]

# Reverse the list
countries.reverse()
print("Reversed List:", countries)

# Print only the middle elements (removing first and last elements)
middle_elements = countries[1:-1]
print("Middle Elements:", middle_elements)


# Q4: Create a list of pin codes, delete the last pincode and the user-required pincode
# Create a list of pin-codes
pin_codes = [110001, 400001, 560001, 700001, 500001]

# Delete the last pincode
pin_codes.pop()
print("After Deleting Last Pincode:", pin_codes)

# Deleting a user-required pincode (let's say 560001)
pin_codes.remove(560001)
print("After Deleting Required Pincode (560001):", pin_codes)

# Q5: Create a list of student names and perform all predefined methods
# Create a list of student names
students = ["John", "Emily", "Michael", "Sarah", "David"]

# Append a student
students.append("James")
print("After Append:", students)

# Insert a student at a specific index
students.insert(2, "Lily")
print("After Insert:", students)

# Remove a student by name
students.remove("Emily")
print("After Remove:", students)

# Pop the last student
students.pop()
print("After Pop:", students)

# Get the index of a student
index_of_sarah = students.index("Sarah")
print("Index of Sarah:", index_of_sarah)

# Sort the list
students.sort()
print("Sorted List:", students)

# Reverse the list
students.reverse()
print("Reversed List:", students)

# Clear the list
students.clear()
print("After Clear:", students)


# outputs:
Original List of Cities: ['New York', 'London', 'Paris', 'Tokyo', 'Berlin', 'Sydney', 'Mumbai', 'Toronto']
After Update: ['New York', 'Los Angeles', 'Paris', 'Tokyo', 'Berlin', 'Sydney', 'Mumbai', 'Toronto']
After Deleting 'Berlin': ['New York', 'Los Angeles', 'Paris', 'Tokyo', 'Sydney', 'Mumbai', 'Toronto']
After Adding 'Singapore': ['New York', 'Los Angeles', 'Paris', 'Tokyo', 'Sydney', 'Mumbai', 'Toronto', 'Singapore']
After Changing 3rd Index Value: [12, 'Hello', 42, True, 'World']
Reversed List: ['France', 'Canada', 'Australia', 'Germany', 'Japan', 'Brazil', 'USA', 'India']
Middle Elements: ['Canada', 'Australia', 'Germany', 'Japan', 'Brazil', 'USA']
After Deleting Last Pincode: [110001, 400001, 560001, 700001]
After Deleting Required Pincode (560001): [110001, 400001, 700001]
After Append: ['John', 'Emily', 'Michael', 'Sarah', 'David', 'James']
After Insert: ['John', 'Emily', 'Lily', 'Michael', 'Sarah', 'David', 'James']
After Remove: ['John', 'Lily', 'Michael', 'Sarah', 'David', 'James']
After Pop: ['John', 'Lily', 'Michael', 'Sarah', 'David']
Index of Sarah: 3
Sorted List: ['David', 'John', 'Lily', 'Michael', 'Sarah']
Reversed List: ['Sarah', 'Michael', 'Lily', 'John', 'David']
After Clear: []



