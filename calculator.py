def addition(a:int,b:int):
    return a+b

def subtract(a:int,b:int):
    return a-b

def division(a:int,b:int):
    try:
        a/b

    except ZeroDivisionError as e:
        return e
