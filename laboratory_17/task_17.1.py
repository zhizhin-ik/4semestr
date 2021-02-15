import numpy as np
import random

# 1
print('№1')
a = np.arange(12, 42)
print("Вектор:\n", a)

# 2
print('№2')
a = np.zeros(12)
a[4] = 1
print("Вектор:\n", a)

# 3
print('№3')
a = np.arange(9).reshape(3, 3)
print("Матрица:\n", a)

# 4
print('№4')
a = np.array([1, 2, 0, 0, 4, 0])
print(a[a > 0])

# 5
print('№5')
a = np.arange(15).reshape(5, 3)
b = np.array([[1, 2],
              [1, 2],
              [1, 2]])
print ("Результат умножения:\n", a.dot(b))

# 6
print('№6')
a = np.zeros((10, 10))
a[1:-1, 1:-1] = 1
print("Матрица:\n", a)

# 7
print('№7')
a = np.random.random(3)
print("Вектор:\n", a)
a.sort()
print("Вектор:\n", a)

# 8
print('№8')
a = np.arange(9).reshape(3, 3)
for i, val in np.ndenumerate(a):
    print(i, val)