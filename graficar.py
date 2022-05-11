
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(int(input("Ingrese valor inicial eje x: ")),int(input("Ingrese valor final eje x: ")),float(input("Ingrese valor de saltos")))
y = np.cos(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafico')
plt.grid()
alt.show()
