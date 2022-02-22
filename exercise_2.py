x = int(input('Введи номер элемента последовательности Фибоначчи: '))


def fibonachi(n):
    if n <= 1:
        return 1
    return fibonachi(n-1) + fibonachi(n-2)
print(fibonachi(x))
