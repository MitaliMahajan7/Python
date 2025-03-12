#Q1)
names=[]
n=int(input("How many names would you like to enter = "))

for _ in range (n):
    name=input("Enter name : ")
    names.append(name)
print("List of Names : ",names)

#Q2)
names=[]
n=int(input("\nHow many names would you like to enter = "))
for _ in range (n):
    name=input("\nEnter name : ")
    names.append(name.upper())
print("List of names in UPPERCASE : ",names)

#Q3)
names=[]
n=int(input("\nHow many names would you like to enter = "))
for _ in range (n):
    name=input("Enter name : ")
    names.append(name.upper()) 
print("List of names in UPPERCASE : ",names)
l=input("Enter the Letter you want to Count :").upper()
l_count=0
for name in names:
    l_count = l_count + name.count(l)
print(f"The Letter {l} appears {l_count} times in the list of names.")

#Q4)
n_len={}
n=int(input("\nHow many names would you like to enter = "))
for _ in range (n):
    name=input("\nEnter name : ")
    n_len[name.upper()]=len(name)
print("Names and their Lengths...\n")
for name, length in n_len.items():
    print(f"{name} : {length} characters")
