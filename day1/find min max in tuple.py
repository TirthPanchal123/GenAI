tuple = (1,2,3,3,4,4,5,6,7,7,8,9,5,3,5,6,3,2,2,3,333,4,3232,132535,2425311,34353422)

'''print(max(tuple))
print(min(tuple))'''

max = tuple[0]
min = tuple[0]

for i in tuple:
    if i>max:
        max = i
    if i<min:
        min =i

print(max)
print(min)