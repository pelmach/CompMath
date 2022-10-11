from math import cos, sin, sqrt, pow


def f(x):
    return sqrt(1 - pow(sin(x), 3))


pr1 = -1.21938
pr2 = -0.151371
x = 1.5
result_1 = 0
result_2 = 0
result_3 = 0
result_4 = 0
minpogr_1 = 100
minpogr_2 = 100
minpogr_3 = 100
minpogr_4 = 100
print("Первая производная:", pr1)
print("Вторая производная:", pr2)
print("  \t h   \t\t    δ1\t\t    δ2\t\t    δ3\t\t    δ4")
for k in range(-2, -16, -1):
    h = 10 ** k
    pr = (f(x+h)-f(x)) / h
    pogr_1 = abs(pr-pr1)
    if pogr_1 < minpogr_1:
        minpogr_1 = pogr_1
        result_1 = pr
    pr = (f(x)-f(x-h)) / h
    pogr_2 = abs(pr-pr1)
    if pogr_2 < minpogr_2:
        minpogr_2 = pogr_2
        result_2 = pr
    pr = (f(x+h)-f(x-h))/(2*h)
    pogr_3 = abs(pr-pr1)
    if pogr_3 < minpogr_3:
        minpogr_3 = pogr_3
        result_3 = pr
    pr = (f(x-h) - 2*f(x) + f(x+h))/pow(h, 2)
    pogr_4 = abs(pr-pr2)
    if pogr_4 < minpogr_4:
        minpogr_4 = pogr_4
        result_4 = pr
    print("For h = 10**({})\t {:.8f}\t {:.8f}\t {:.8f}\t {:.8f}".format(k, pogr_1, pogr_2, pogr_3, pogr_4))

print("1. f'({}) = {:.8f}".format(x, result_1))
print("2. f'({}) = {:.8f}".format(x, result_2))
print("3. f'({}) = {:.8f}".format(x, result_3))
print("4. f''({}) = {:.8f}".format(x, result_4))

