"""
x(n) = u(n-5)
"""
from pylab import *

c = [0,0,0,0,0]
b = ones(95)#hacer 1 los elementos restantes
y = np.append(c,b)#agregar a continuacion los vectores c y b
x = linspace(1, 100, 100) # de 1 a 100 con 100 muestras

markerline, stemlines, baseline = stem(x, y, '-.') #stem que grafica 
setp(markerline, 'markerfacecolor', 'b')#diferentes estilos de marcador
setp(baseline, 'color','r', 'linewidth', 2)#diferentes estilos de línea

#etiquetas
xlabel("xlabel")
ylabel("ylabel")



print(y)
show()