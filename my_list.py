# Create an empty list
my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


# Extend the list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort the list
my_list.sort()

# Find the index of 30
index_of_30 = my_list.index(30)

print(my_list)
print("Index of 30:", index_of_30)