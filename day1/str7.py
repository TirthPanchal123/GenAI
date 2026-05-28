s =input("enter a string:")

lst = s.split()
print(lst)


num = lst[0]

for i in lst:
    if len(i)>len(num):
        num = i
print(num)