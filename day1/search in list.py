a=[1,2,3,4,5,6,7,8,9,0, "tirth"]

value = input("enter number to find that num's index:")

if (value in a):
    
    index_number = a.index(value)
    print(index_number)
    
else:
    print("your entered number isnot in list ")