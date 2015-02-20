"""
x(n) = (0.9)^n*sen(0.25n)
"""
from pylab import *

x = linspace(1, 100, 100) # de 1 a 100 con 100 muestras

markerline, stemlines, baseline = stem(x, pow(0.9,x)*sin(0.25*x), '-.') #stem que grafica 
setp(markerline, 'markerfacecolor', 'b')#diferentes estilos de marcador
setp(baseline, 'color','r', 'linewidth', 2)#diferentes estilos de línea

#etiquetas
xlabel("xlabel")
ylabel("ylabel")

show()