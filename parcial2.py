import numpy as np
from math import sin, pi, exp, floor
from matplotlib import pyplot as plt
import scipy.constants as sc 

#############################################

#Variables

Nptos = 2001
pc = 500
Ez = np.zeros((1,Nptos), dtype = float)
Hy = np.zeros((1,Nptos), dtype = float)
eps = np.zeros((1,Nptos), dtype = float)
eps[:500] = sc.epsilon_0
eps[501:1501] = 12*sc.epsilon_0
eps[1501:] = sc.epsilon_0
dt = 0.1e-12
# dx =  0.054
dx = 0.00127 # 1.27/(N-1) => 1.27/1000
E0 = 1.0
#############################################
w = 10E9
Ttotal = floor(1/(dt*w)) #(100*0.18e-9 = 180 ns)
Ez[0, pc] = E0*exp((-(i - 8.0)**2)/16.0)

X0 = np.linspace (-1, 1, num = Nptos)*dx
for i in range(0, Ttotal):
    #actualiza el campo magnético
    for j in range(0, (Nptos -1)):
        Hy[0, j] = Hy[0, j] + (dt/(sc.mu_0*dx))*(Ez[0, j + 1] - Ez[0,j])
    #Actualiza el campo eléctrico
    for k in range(0, Nptos):
        Ez[0, k] = Ez[0, k] + (dt/(eps[0,k]*dx))*(Hy[0, k] - Hy[0, k - 1])
    #Fuente del campo eléctrico
    
#############################################

#Gráficas

    plt.plot(X0, Ez[0,:])
    plt.clear()
    plt.ylabel("Campo Electrico (V/m)")
    plt.xlabel("Posición (m)")
    plt.xlim(-1.5, 1.5)
    plt.show()

