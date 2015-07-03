import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print("2015-3-25")

now()
print(now.__name__)

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@logger("DEBUG")
def today():
    print("2015-3-25")

today()
print(today.__name__)

def beginend(func):
    def wrapper(*args,**kw):
        print("call %s():" % func.__name__)
        func(*args,**kw)
        print("end %s():" % func.__name__)
        return
    return wrapper

@beginend
def printdate():
    print("2015-7-3")

printdate()
