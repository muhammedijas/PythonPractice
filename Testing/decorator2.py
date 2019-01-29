# in decorator, we send function as argument

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print ('Original function name is . {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print ('Display is running')

@decorator_function
def display_info(name,age):
    print('display_info ran with the information {},{}'.format(name,age))
#run_display=decorator_function(display) is similar to @decorator_function
#run_display()


display_info('Ijas',21)
display()
