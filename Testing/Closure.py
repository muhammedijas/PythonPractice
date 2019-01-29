# to print out the inner function with out execution, remove the paramter

def outer_func():
    wrd='Hi'

    def inner_func():
        print(wrd)
    return inner_func()

of=outer_func()


