#Functions
#Imp Points :
#A parameter is the variable listed inside the parentheses in the function definition.
#An Argument is the value that is sent to the function when it is called.

#Q1
'''
1)Create a function getting two integer inputs from user. & print the following:

Addition of two numbers is +value
Subtraction of two numbers is +value
Division of two numbers is +value
Multiplication of two numbers is +value

Here the value represents math function associated
'''

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


#---------------------------------------
#2. Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree
#Here we are using default argument
#Default value can be changed
def covid(name,temperature=98):
    print(name,"has ",temperature,"body temp")
    if (temperature!=98):
        print("Corona positive")
    else:
        print("Corona Negative")

name=input()
temp=int(input())
covid(name,temp)
