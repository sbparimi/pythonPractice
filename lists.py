# print even numbers using list comprehension
numbers = [1,2,3,4,5,6,7,8]
result = [n * n for n  in numbers if n%2==0]
#print(result)

# print (letter pair) for abcd for each number in 0123 
PairedList = []
for eachLetter in "abcd":
    for eachNumber in "0123":
        PairedList.append((eachLetter, int(eachNumber)))
print(PairedList)

# Using the list comprehension
PairedList2 = [(eachLetter,eachNumber) for eachLetter in "abcd" for eachNumber in range(4) ]
print("This is the Paired list 2", PairedList2)


# Dictionary comprehensions using zip 
names = ['Suresh','Ramesh','Somesh','Mahesh']
roles = ['QA','Dev','DevOps','SDET']

my_dict = {name:role for name,role in zip(names,roles)}
print("This is dict comprehension", my_dict)