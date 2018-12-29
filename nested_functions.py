def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()

def outer2():
    x = 'outer x'
    def inner2():
        #x = 'inner x'
        print(x)
    inner2()
    print(x)

outer2()
