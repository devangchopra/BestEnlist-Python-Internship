#Wap to merge two dictionaries

D1 = {"Apple":"Fruit ", "Potato":"Vegetable"}
D2 = {"Mango":"Fruit", "Onion":"Vegetable"}
D3 = {**D1,**D2}
print(D3)

#Wap to remove a key from dictionary

A1={"Plant":"Living","Desk":"Non-Living","Human":"Living"}
del A1["Desk"]
print(A1)

#Wap to map two lists into dictionary

L1=["One","Two","Three"]
L2=[1,2,3]
LD={}
for i in range(3):
    LD[L1[i]]=L2[i]
print(LD)

#Wap to find length of a set

CSK = {"dhoni", "bravo", "jadeja"}
print(len(CSK))

#Write a Python program to remove the intersection of a 2nd set from the 1st set

S1 = {1,2,3,4,5}
S2 = {4,5,6,7,8}
print(S1-S2)

