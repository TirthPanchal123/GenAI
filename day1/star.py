'''def  total(*nums):
    return sum(nums)

print(total(1,2,3,4))'''


def info(**kwargs):
    for key, value in kwargs.items():
        print(f"my {key} is {value}")
info(name='tirth',age=23)