def add(*args):
    # *args is an unlimited number of arguments
    # * is asteriks
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2, 3, 4, 6, 7))

def calculator(**kwargs):
    # **  two asteriks signs in front of parameter name, we have created unlimited keyword arguments.
    pass
