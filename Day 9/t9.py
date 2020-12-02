#Create a lambda function that multiplies argument x with argument y

a = lambda b, c : b * c
print(a(20, 30))

#-------------------------------------

#Write a Python program to create Fibonacci series to n using Lambda

def fibonacci(limit):
    listA = [0, 1]
    any(map(lambda _:listA.append(sum(listA[-2:])),
         range(2, count)))
    return listA[:count]
print("Enter Limit")
limit=int(input())
print(fibonacci(limit))
print('\n')

#----------------------------------

#Write a Python program that multiply each number of given list with a given number

arr = [101, 202, 303, 404, 505]
value = 5
ans=list(map(lambda arr : arr * value, arr))
print(arr)

#---------------------------------------

#Write a Python program to find numbers divisible by 9 from a list of numbers

arr = [101,102,103,104,105]
ans = list(filter(lambda x: (x % 9 == 0), arr))
print(ans)

#--------------------------------------

# Exercise 5 - Write a Python program to count the even numbers in a given list of integers

arr=[1,2,3,4,5,6,7,8,9,10]
even = (list(filter(lambda x: (x % 2 == 0) , arr))
ans=len(even)
print(ans)
#---------------------------------
