# 1. Write a Python program to Get Only unique items from two sets.
#Input:
# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Combine the sets
combined_set = set1.union(set2)

# Print the output
print("Unique items:", combined_set)


#2. Write a Python program to Return a set of elements present in Set A or B, but
#not both.
#Input:
# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Get elements present in Set A or B but not both
unique_elements = set1.symmetric_difference(set2)

# Print the output
print(unique_elements)


# 3 Write a Python program to Check if two sets have any elements in common. If
#yes, display the common elements.
#Input:
# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Find common elements
common_elements = set1.intersection(set2)

# Check if there are any common elements and display them
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements.")


# 4. Write a Python program to Remove items from set1 that are not common to
#both set1 and set2.
#Input:
# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Keep only the common elements in set1
set1.intersection_update(set2)

# Print the output
print("Updated set1 with common elements:", set1)



