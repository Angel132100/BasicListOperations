
color_list = ["red", "green", "blue", "yellow"]
# Access the first element
print(color_list[0])  # Output: 'red'


print(color_list[-1])  # Output: 'yellow'



num_list = [4, 6, 4, 2, 9, 4, 1]


num_list.append(5)


num_list.remove(4)
# Count occurrences of '4'
print(num_list.count(4))


num_list.count(4)
# Find the index of '9'
print(num_list.index(9))


fruit_list = ["apple", "banana", "cherry"]
fruit_list[1] = "orange"
fruit_list.pop()
print(fruit_list)