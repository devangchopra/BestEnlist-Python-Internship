#WAP to loop through a list of numbers and add +2 to every value to elements in list

list =[10,20,30,40,50]
#Index from 0-4
#Loop runs one less
for i in range(5):
    list[i]=list[i]+2
print(list)

#-----------------------------
'''
WAP to get the below pattern
54321
4321
321
21
1
'''
for i in range(5,1,-1):
    j=i
    while j>1:
        print(j,end='')
        j-=1
    print(j)

#------------------------------------

#Python Program to Print the Fibonacci sequence
n = int(input())
FT = 0
A1 = 0
A2 = 1
if n == 1:
    print(A1)
else:    
    while FT < n:
        print(A1, end =', ')
        C = A1 + A2
        
        A1 = A2
        A2 = C
        FT+= 1

#-------------------------------------

#Explain Armstrong number and write a code with a function
n= int(input())  
sum = 0  
f = n    
while f > 0:
    digit = n % 10
    sum += digit ** 3
    f//= 10
if n == sum:
    print("Yes")  
else:
    print("No")

#-------------------------------------

#Write a program to print the multiplication table of 9
n=int(input())
for i in range(n):
    print(9*n)
    n=n-1

#---------------------------------
    
#Check if a program is negative or positive
n=int(input())
if(n>0):
    print("Positive")
else:
    print("Negative")

#-----------------------------

#Write a program to convert the number of days to ages

n=int(input())
print("Age is",n//365)

#----------------------------

#Solve Trigonometry problem using math function write a program to solve us-ing math function
import math

A = float(input())
print('sin(',A,') = ', math.sin(math.radians(theta)))
print('cos(',A,') = ', math.cos(math.radians(theta)))
print('tan(',A,') = ', math.tan(math.radians(theta)))

#-------------------------

#Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
def add(x,y):
    return x+y
def sub(x,y):
    if(x>y):
        return x-y
    else:
        return y-x
def mult(x,y):
    return x*y
def div(x,y):
    #For Decimal / Not Rounded Division
    return x/y
def fdiv(x,y):
    #For Floor division
    return x//y

x=int(input())
y=int(input())
print("Addition is ",add(x,y))
print("Subtraction is ",sub(x,y))
print("Multiplication is ",mult(x,y))
print("Division is " ,div(x,y))
print("Floor Division is" ,fdiv(x,y))
