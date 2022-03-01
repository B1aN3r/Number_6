def inspect(f):
    slovar = {}
    def wrap(*args, **kwargs):
        Args = f(*args)
        slovar[args] = Args
        print(slovar.values())
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
concat('Hello', ' ', 'Aboba', **b)
