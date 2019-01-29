# in decorator, we send function as argument

def decorator_function(original_function):
    def wrapper_function():
        print ('Original function name is . {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print ('Display is running')

#run_display=decorator_function(display) is similar to @decorator_function
#run_display()

display()

