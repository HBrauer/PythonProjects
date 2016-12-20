import math
import numpy as np
import matplotlib.pyplot as plt
T = 1/1000
x = [y*T for y in range(0, 1000)]
print(x)
y = [ math.sin(2*1*math.pi*v)*math.sin(2*50*math.pi*v) for v in x]
#y = [ math.sin(2*50*math.pi*v+0.95*math.pi) + math.sin(2*50*math.pi*v) for v in x]
print(y)
N = len(x)

xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
print(1.0/(2.0*T))
yf = np.fft.fft(y)
print(yf)
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(x, y)
ax1.set_ylim([-2,2])

ax2 = fig.add_subplot(212)
ax2.plot(xf, 2.0/N * np.abs(yf[0:N/2]))
plt.show()


