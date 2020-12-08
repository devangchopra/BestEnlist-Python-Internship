#WAP using zip() function and list() function :

#Create a merged list of tuples from the two lists given.
L1 = [101,102,103,104,105]
L2 = [201,202,203,204]
ZL= list(zip(L1,L2))

print(ZL)
print("\n")

#----------------------------------------------------

#First create a range from 1 to 8. Then using zip merge the given list and the range together to create a new list of tuples.

N1 = [x for x in range(1, 9)]
N2 = [40, 25, 398, 500, 125, 258, 89, 147, 22]
zll = list(zip(N1, N2))
print(zll)
print("\n")

#----------------------------------------------

#Using sorted() function, sort the list in ascending order.
A1= [999, 949,9245, 55152, 7452]
print(sorted(A1))

#------------------------------------------------

#WAP using filter function
# filter the even numbers so that only odd numbers are passed to the new list.
print("Enter no.")
ip = map(lambda x: int(x), input().split())
en = list(filter(lambda x: x % 2 == 0, ip))
print("Even numbers", en)

#----------------------------------------
