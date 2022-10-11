import math


def f(x):
    return math.sqrt(abs(x - math.pi))

def lagrange(x, ends, steps):
    result = 0
    step = (ends[1] - ends[0]) / (steps - 1)
    xi = []
    for i in range(steps):
        xi.append(ends[0] + step * i)
    for k in range(steps):
        up = 1
        for i in range(steps):
            if (k != i):
                up *= x - xi[i]
        down = 1
        for i in range(steps):
            if (k != i):
                down *= xi[k] - xi[i]
        result += up / down * f(xi[k])
    return result


def chebishev(x, ends, steps):
    result = 0
    xi = []
    for i in range(steps + 1):
        xi.append((ends[1] + ends[0]) / 2 + (ends[1] - ends[0]) / 2 * math.cos((2 * i + 1) * math.pi / 2 / (steps + 1)))
    xi.sort()
    print(xi)
    for k in range(steps):
        up = 1
        for i in range(steps):
            if (k != i):
                up *= x - xi[i]
        down = 1
        for i in range(steps):
            if (k != i):
                down *= xi[k] - xi[i]
        result += up / down * f(xi[k])
    return result


def calc1(ends, steps):
    points = 100
    step = (ends[1] - ends[0]) / (points - 1)
    pogr = 0
    for i in range(points):
        x = ends[0] + step * i
        y1 = chebishev(x, ends, steps)
        y2 = f(x)
        if abs(y1 - y2) > pogr:
            pogr = abs(y1 - y2)
    print("Для {0} узлов максимальная погрешность: {1:.13f}".format(steps, pogr))


def calc(ends, steps):
    points = 100
    step = (ends[1] - ends[0]) / (points - 1)
    pogr = 0
    for i in range(points):
        x = ends[0] + step * i
        y1 = lagrange(x, ends, steps)
        y2 = f(x)
        if abs(y1 - y2) > pogr:
            pogr = abs(y1 - y2)
    print("Для {0} узлов максимальная погрешность: {1:.13f}".format(steps, pogr))


print("Равномерная сетка")
edge = [-3, 3]
calc(edge, 25)
calc(edge, 65)
calc(edge, 85)
print("Сетка Чебышева")
calc1(edge, 15)
calc1(edge, 35)
calc1(edge, 55)
