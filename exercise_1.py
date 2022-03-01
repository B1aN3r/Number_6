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

b = {'reverse': True}
concat('Hello', ' ', 'Aboba', **b)