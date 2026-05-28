list =[1,4,2,5,6,74,3,6,5335,6575,2423,6,64373532,436754,632]

position = int(input("enter number you want to highest:"))

def highest(list,position):
    list.sort(reverse=True)
    return list[position-1]

print(highest(list,position))