"""
x(n) = 3*sen(0.2n)
"""
from pylab import *

x = linspace(1, 100, 100) # de 1 a 100 con 100 muestras

markerline, stemlines, baseline = stem(x, 3*sin(0.2*x), '-.') #stem que grafica 
setp(markerline, 'markerfacecolor', 'b')#diferentes estilos de marcador
setp(baseline, 'color','r', 'linewidth', 2)#diferentes estilos de línea

#etiquetas
xlabel("xlabel")
ylabel("ylabel")


show()