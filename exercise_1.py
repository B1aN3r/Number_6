def concat(*args, reverse=False):
    res = ''
    if reverse:
        args = reversed(args)
        for el in args:
            res += el
        print(res)
    else:
        for el in args:
            res += el
        print(res)


elem = ['Hello', ' ', 'Aboba']
b = {'reverse': True}
result = concat(*elem, **b)
