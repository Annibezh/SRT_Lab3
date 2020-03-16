import numpy as np
import random
from math import sin, cos, pi
import matplotlib.pyplot as plt

n = 10   # number of harmonics
w = 900  # the highest frequency
N = 256  # number of signals
number = w/(n - 1)  # the difference between harmonics

# frequency generation
W = lambda n, w: w - n * number
w_values = [W(n, w) for n in range(n)]
x = np.zeros(N)

def plot(function):
    plt.figure(figsize=(20, 15))
    plt.plot(function)
    plt.grid(True)
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
F_real = np.zeros(N)
F_im = np.zeros(N)

for p in range(N):
    for k in range(N):
        F_real[p] += x[k] * cos(2*pi/N * p * k)
        F_im[p] += x[k] * sin(2*pi/N * p * k)
for i in range(N):
    F[i] += F_real[i] + F_im[i]

plot(F)

def multi_plot(y1, y2, y3):
    plt.figure(figsize=(20, 15))
    plt.plot(y1, 'b', label="F_real")
    plt.plot(y2, 'k', label="F_im")
    plt.plot(y3, 'r', label="F sum")
    plt.grid(True)
    plt.legend(prop={'size': 16}, loc='upper right', borderaxespad=0.)
    plt.show()

multi_plot(F_real, F_im, F)
