"""
Декораторы
 1. Функции можно возвращать из функции

"""






def log_decorator(func):
    def wrap(*args,**kwargs):
        print(f'Calling func {func.__name__}')
        func(*args,**kwargs)
        print(f'args: {args} ')
        print(f'kwargs: {kwargs} ')
    return wrap

@log_decorator
def hello_world(name):
    print("HW "+str(name))



if __name__ == '__main__':
    hello_world('Djohn')
