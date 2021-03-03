def add(*args):
    sum = 0
    for i in args:
        print(i)
        sum = sum+i
    return sum

s = add(5,4,8,6,8,9,4,6,1,2,5,8)
print(s)