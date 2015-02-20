"""
x(n) = 2*cos(0.25*n)+1.5*sin(0.25*n)-cos(0.1*n)
"""
from pylab import *

n = linspace(1, 100, 100) # de 1 a 100 con 100 muestras

markerline, stemlines, baseline = stem(n, 2*cos(0.25*n)+1.5*sin(0.25*n)-cos(0.1*n), '-.') #stem que grafica 
setp(markerline, 'markerfacecolor', 'b')#diferentes estilos de marcador
setp(baseline, 'color','r', 'linewidth', 2)#diferentes estilos de línea

#etiquetas
xlabel("xlabel")
ylabel("ylabel")

show()