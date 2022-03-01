def inspect(f):
    def wrap(*args, **kwargs):
        print(f'входные данные : {args} и {b}')
        print(f'Args: {args}')
        print(f'Kwargs: {b}')
        print(f'Retvalue: {f(*args, **kwargs)}')
        print(f(*args))
        return f(*args)
    return wrap

@inspect
def concat(*args, reverse=False):
    res = ''
    if reverse:
        args = reversed(args)
        for el in args:
            res += el
        return res
    else:
        for el in args:
            res += el
        return res

b = {'reverse': True}
concat('Hello', ' ', 'Aboba')