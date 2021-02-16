import math
import numpy as np
import pylab


def func(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)

# Строим график
xmin = 1.0
xmax = 15.0
dx = 0.01
xlist = np.arange(xmin, xmax, dx)
ylist = [func(x) for x in xlist]
pylab.plot(xlist, ylist)
# Исходный график синего цвета

# 2 точки
A = np.array([[1, 1], [1, 15]])
b = np.array([func(1), func(15)])
xres = np.linalg.solve(A, b)
yres = [(xres[0]+xres[1]*x) for x in xlist]
pylab.plot(xlist, yres)
# График оранжевого цвета
# Плохо апроксимирует

# 3 точки
A = np.array([[1, 1, 1], [1, 8, 64], [1, 15, 225]])
b = np.array([func(1), func(8), func(15)])
xres = np.linalg.solve(A, b)
yres = [(xres[0]+xres[1]*x+xres[2]*x*x) for x in xlist]
pylab.plot(xlist, yres)
# График зеленого цвета
# Плохо апроксимирует, но но лучше прошлого

# 4 точки
A = np.array([[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]])
b = np.array([func(1), func(4), func(10), func(15)])
xres = np.linalg.solve(A, b)
print(xres)
yres = [(xres[0]+xres[1]*x+xres[2]*x*x+xres[3]*x*x*x) for x in xlist]
pylab.plot(xlist, yres)
# График красного цвета
# Хорошо апроксимирует
pylab.show()
