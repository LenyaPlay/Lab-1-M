import math
import draw

a = - 8
b = - 7.5

def f(x):
    return math.exp(x) + math.sin(2 * x) + 0.5

def df(x):
    return math.exp(x) + 2 * math.cos(2 * x)

def ddf(x):
    return math.exp(x) - 4 * math.sin(2 * x)

def equitonHasOneRoot(a, b, f, df):
    if (f(a) > 0 and f(b) < 0) or (f(a) < 0 and f(b) > 0):
        if df(a) > 0 and df(b) > 0 or df(a) < 0 and df(b) < 0:
            return True
    return False

def getConstC(x, df, eps):
    if df(x) < 0:
        return -2 / df(x) + eps
    if df(x) > 0:
        return -2 / df(x) - eps

def getX0(a, b, f, ddf):
    if f(a) * ddf(a) > 0:
        return a
    if f(b) * ddf(b) > 0:
        return b
    return max(a, b)  # Если ничего не сошлось

eps = 10 ** -3
d = 10 ** -2

def beautifulPrint(*args, size):
    str = ''
    for arg in args:
        str += f'{arg:<{size}}'
    print(str)

def writeInfoAndCheckCondition(i, xn, xn1, fn, fn1):
    if math.fabs(xn1 - xn) < eps and math.fabs(fn1 - fn) < d:
        print("Итог: ")
        beautifulPrint(i, xn, xn1, math.fabs(xn1 - xn), math.fabs(fn1 - fn), size=24)
        print(f'Итоговое значение функции: {fn1} \n')
        return True
    beautifulPrint(i, xn, xn1, math.fabs(xn1 - xn), math.fabs(fn1 - fn), size=24)
    return False

def Iterator(c, x0, iter_func, name):
    print(f'{name:^100}')
    beautifulPrint("Итерация", "xn", "xn1", "math.fabs(xn1 - xn)", "math.fabs(fn1 - fn)", size=24)
    xn = x0
    fn = f(xn)
    i = 0
    while True:
        i += 1
        xn1 = iter_func(c, x0, xn, f, df, ddf)
        fn1 = f(xn1)
        if writeInfoAndCheckCondition(i, xn, xn1, fn, fn1):
            break
        xn = xn1
        fn = fn1

def MPI(c, x0, xn, f, df, ddf):
    return xn + c * f(xn)

def Newton(c, x0, xn, f, df, ddf):
    return xn - f(xn) / df(xn)

def ModNewton(c, x0, xn, f, df, ddf):
    return xn - f(xn) / df(x0)


if not equitonHasOneRoot(a, b, f, df):
    print("Больше одного корня")
else:
    print("Имеет только один корень")

Iterator(c=getConstC(a, df, eps), x0=a, iter_func=MPI, name = 'МПИ')
Iterator(c=None, x0=getX0(a, b, f, ddf), iter_func=Newton, name = 'Нъютона')
Iterator(c=None, x0=getX0(a, b, f, ddf), iter_func=ModNewton, name = 'Мод. Нъютона')

draw.draw_function(-15, 15,f)



