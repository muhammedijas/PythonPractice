from functools import wraps
def my_logger(original_function):
    import  logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__),level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args,**kwargs):
        logging.info(
            'ran with args: {} and kwargs: {}'.format(args, kwargs)
        )
        return original_function(*args,**kwargs)
    return wrapper


def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args,**kwargs):
        t1=time.time()
        result = original_function(*args,**kwargs)
        t2=time.time()-t1
        print('the function {} ran in {} sec'.format(original_function.__name__,t2))
        return result
    return wrapper

import time

#@my_timer
#@my_logger
def display_info(name,age):
    time.sleep(2)
    print('display_info ran with the information {},{}'.format(name,age))
#run_display=decorator_function(display) is similar to @decorator_function
#run_display()

display_info=my_timer(my_logger(display_info))

print(display_info.__name__)
display_info('Ijas',21)

