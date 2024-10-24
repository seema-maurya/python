# 1. Write a Python program and calculate the mean of the below dictionary.
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
# Calculate the mean
mean_value = sum(test_dict.values()) / len(test_dict)
# Print the output
print(mean_value)


# 2.Write a Python script to concatenate the following dictionaries to create a new one.
# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Method 1: Using the update() method
result_dict = dic1.copy()  # Make a copy of dic1
result_dict.update(dic2)   # Update with dic2
result_dict.update(dic3)   # Update with dic3

# Print the result
print("Concatenated Dictionary (using update):", result_dict)

# Method 2: Using dictionary unpacking (Python 3.5+)
result_dict_unpacking = {**dic1, **dic2, **dic3}

# Print the result
print("Concatenated Dictionary (using unpacking):", result_dict_unpacking)


# 3.Write a Python program to get the key, value and item in a dictionary.
# Define the dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Get and print keys
print("Keys:")
for key in dict_num.keys():
    print(key)

# Get and print values
print("\nValues:")
for value in dict_num.values():
    print(value)

# Get and print items (key-value pairs)
print("\nKeys " " values:")
for item in dict_num.items():
    print(item)


# Write a Python program to get the key, value and item in a dictionary.
# Define the dictionary
input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

# Get and print keys
print("Keys:")
for key in input_dict.keys():
    print(key)

# Get and print values
print("\nValues:")
for value in input_dict.values():
    print(value)

# Get and print items (key-value pairs)
print("\nItems:")
for item in input_dict.items():
    print(item)

