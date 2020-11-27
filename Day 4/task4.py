# Exercise 1
# WAP to create a list of n integer values and do the following
#(List Behaves as Vector)

L1 = []
print("Enter no. of Elements")
n = int(input())
for i in range(0, n):
    a= int(input())
    L1.append(a)
print(L1)


# Add an item in to the list
L1.insert(2,10)
print(L1)
print('\n')


# Delete
del L1[2]
print(L1)
print('\n')


# Store the smallest number from the list to a variable
low = min(L1)
print("Smallest Number")
print(low)
print('\n')


# Store the largest number from the list to a variable
high = max(L1)
print("Larget Number")
print(high)
print('\n')

print("Modified List")
print(L1[0:])
print('\n')


# Exercise 2 Create a tuple and print the reverse of created tuple
tuple = ('apple', '10', 'fruit', '32.0')
rtuple = tuple[::-1]
print("Reversed tuple")
print(rtuple)
print('\n')

# Exercise 3 Create a tuple and convert tuple into list
list = []
tuple = ('hello', '15', '3.14', 'bye', 'no')
for i in range(5):
    list.append(tuple[i])
print("Converted list from tuple")
print(list[0:5])
