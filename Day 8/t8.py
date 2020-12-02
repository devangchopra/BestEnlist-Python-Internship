#List down all the error types and check all the errors using a py-thon program for all errors

# 1 Zero Division Error
try:
    print(50 / 0)
except ZeroDivisionError:
    print("Division By Zero is not possible")

# 2 Index Error
arr = [15, 20, 25]
try:
    print(arr[5])
except IndexError:
    print("Out Of Range")

# 3 Key Error
dicti = {"1" : 'a', "2" : 'b', "3" : 'c'}
try:
    print(dicti["6"])
except KeyError:
    print("Key Not Found")

# 4 Module Not Found Error
try:
    import flask
except ModuleNotFoundError:
    print("Module not found")

#-------------------------------------------------------------

# Exercise 2 - Design a simple calculator app with try and except for all use cases

symbols = "+ - x / % \n"
try:
    i1 = int(input("Enter First Number"))
    print(symbols)
    choice = input("Enter Your Symbol")
    i2 = int(input("Enter Second Number"))
    if choice in symbols:
        if choice == '+':
            print(i1 + i2)
        elif choice == '-':
            if (i1>i2) :
                print(i1-i2)
            else:
                print(i2-i1)        
        elif choice == 'x':
            print(i1*i2)
        elif choice == '/':
            print(i1/i2)
        elif choice == '%':
            print(i1%i2)
except ValueError:
    print("Number Not Correct")
except ZeroDivisionError:
    print("Division by Zeronot possible")

#-----------------------------------------------------------------

# Exercise 3 - Print one message if the try block raises a NameError and another for other errors
try:
    print(A)
except NameError:
      print("A is not defined")
except:
      print("Unknown Error")

#------------------------------------------------------------

# Exercise 4 -  When try-except scenario is not required?

#We can use try except to stop error coming at running time but most of the errors are displayed at interpretation
#time in python . We should always try to resolve errors at compile / interpretation time. 

#-------------------------------------------------------------


# Exercise 5 - 	Try getting an input inside the try catch block
try:
    num = int(input("Enter"))
except ValueError:
    print("Invalid Input")

#-------------------------------------------
