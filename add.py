import numpy as np
import random
from math import sin, cos, pi
import matplotlib.pyplot as plt
import time

n = 10   # number of harmonics
w = 900  # the highest frequency
N = 256  # number of signals
number = w/(n - 1)  # the difference between harmonics

# frequency generation
W = lambda n, w: w - n * number
w_values = [W(n, w) for n in range(n)]
x = np.zeros(N)


def plot(function):
    plt.figure(figsize=(10, 5))
    plt.plot(function)
    plt.grid(True)
    plt.show()


def multi_plot(y1, y2, y3):
    plt.figure(figsize=(10, 5))
    plt.plot(y1, 'b', label="F_real")
    plt.plot(y2, 'k', label="F_im")
    plt.plot(y3, 'r', label="F sum")
    plt.grid(True)
    plt.legend(prop={'size': 16}, loc='upper right', borderaxespad=0.)
    plt.show()

#generating random signal
random.seed(42)
for j in range(n):
    amplitude = random.choice([i for i in range(-10, 10) if i != 0])
    phi = random.randint(-360, 360)
    for t in range(N):
        x[t] += amplitude * sin(w_values[j] * t + phi)

plot(x)

F = np.zeros(N)
F_new = np.zeros(N)
F_real = np.zeros(N)
F_im = np.zeros(N)

F_real_w = np.zeros(N)
F_im_w = np.zeros(N)

# таблиця коефіцієнтів w[p][k] від N
w_coeff = np.zeros(shape=(N, N))
for p in range(N):
    for k in range(N):
        w_coeff[p][k] = cos(2*pi/N * p * k) + sin(2*pi/N * p * k)

start1 = time.time()
for p in range(N):
    for k in range(N):
        F_real[p] += x[k] * cos(2*pi/N * p * k)
        F_im[p] += x[k] * sin(2*pi/N * p * k)
for i in range(N):
    F[i] += F_real[i] + F_im[i]
time1 = time.time() - start1
print(f"Time without w_pkN table: {time1}")

plot(F)

multi_plot(F_real, F_im, F)

# Робимо те саме, але з використання таблиці
start2 = time.time()
for p in range(N):
    for k in range(N):
        F_real_w[p] += x[k] * w_coeff[p][k]
        F_im_w[p] += x[k] * w_coeff[p][k]
for i in range(N):
    F_new[i] += F_real_w[i] + F_im_w[i]
time2 = time.time() - start2

print(f"Time with w_pkN table: {time2}")

multi_plot(F_real_w, F_im_w, F_new)
