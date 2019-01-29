# instead of decorator function, class has came and oricinal function declared in init

class decorator_class:
    def __init__(self,original_function):
        self.original_function=original_function
# call is used instead of wrapper
    def __call__(self, *args, **kwargs):
        print('Original function name is . {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print ('Display is running')

@decorator_class
def display_info(name,age):
    print('display_info ran with the information {},{}'.format(name,age))
#run_display=decorator_function(display) is similar to @decorator_function
#run_display()


display_info('Ijas',21)
display()
