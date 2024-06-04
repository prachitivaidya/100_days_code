def add(*args):
    sum =0
    for arg in args:
        sum += arg
    return sum

print(add(1,2,3,4))

def calculate(n,**kwargs):
    # print(kwargs)
    # for(key,value) in kwargs.items():
    #     print(key,value)

    n += kwargs["add"]
    n += kwargs["sub"]
    print(n)
calculate(2,add =3, sub =4, multiply =9)

class Car:

    def __init__(self,**kwargs):
