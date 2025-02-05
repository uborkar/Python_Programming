Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
my_list = [1, 2, 3, 4, 5]
print (my_list)
[1, 2, 3, 4, 5]
print(type(my_list))
<class 'list'>
my_list2 = ['Sam','Shawn','Alice','Tom','Smith']
print (my_list2)
['Sam', 'Shawn', 'Alice', 'Tom', 'Smith']
# Accessing List Elements

print(my_list[0])
1
print(my_list[-1])
5
print(my_list[1:3])
[2, 3]

#Adding Elements
my_list2 = ['Sam','Shawn','Alice','Tom','Smith']
my_list2.append('Pawl')
print(my_list2)
['Sam', 'Shawn', 'Alice', 'Tom', 'Smith', 'Pawl']
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 'a')
print(my_list)
[1, 2, 'a', 3, 4, 5]
# Extend (Adding Multiple Elements)
my_list.extend([7, 8])
print(my_list)
[1, 2, 'a', 3, 4, 5, 7, 8]

 #Removing List Elements

my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)
[1, 2, 4, 5]

my_list = [1, 2, 3, 4, 5]
popped_value = my_list.pop(2)  # Removes and returns the element at index 2 ('a')
print(popped_value)
3
print(my_list)
[1, 2, 4, 5]

my_list = [1, 2, 3, 4, 5]
my_list.clear()  # []
print(my_list)
[]

#Finding Elements from list
#Method 1 : Through Index
my_list = [1, 2, 3, 4, 5]
my_list.index(4)  # Returns the index of 4, which is 2
3
#Method 2: Through Count
my_list = [1, 2, 3, 4, 5]
my_list.count(3)  # Counts how many times 3 appears in the list
1

# Sorting and Reversing
# Sorting my_list2
my_list2 = ['Sam','Shawn','Alice','Tom','Smith']
my_list.sort()
print(my_list2)
['Sam', 'Shawn', 'Alice', 'Tom', 'Smith']
my_list2.sort()
print(my_list2)
['Alice', 'Sam', 'Shawn', 'Smith', 'Tom']


#Reversing List 2
>>> my_list2 = ['Sam','Shawn','Alice','Tom','Smith']
>>> my_list2.reverse()
>>> print (my_list2)
['Smith', 'Tom', 'Alice', 'Shawn', 'Sam']
>>> 
>>> 
>>> #List Comprehension
>>> squares = [x**2 for x in range(6)]  # [0, 1, 4, 9, 16, 25]
>>> print(squares)
[0, 1, 4, 9, 16, 25]
>>> 
>>> #Length of list
>>> len(my_list)  # Returns the length of the list
5
>>> 
>>> 
>>> #Concatenating Lists
>>> list1 = [1, 2]
>>> list2 = [3, 4]
>>> merged_list = list1 + list2
>>> print(merged_list)
[1, 2, 3, 4]
>>> #Repeatation of list
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list = [1, 2] * 3
>>> 
>>> print(my_list)
[1, 2, 1, 2, 1, 2]
>>> 
>>> #Nested Lists
>>> nested_list = [[1, 2], [3, 4], [5, 6]]
>>> print (nested_list)
[[1, 2], [3, 4], [5, 6]]
>>> 
>>> 
>>> 
>>> 
