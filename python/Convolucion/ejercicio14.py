"""
h=[4 3 2 1] *conv* x=[1 2]
"""
from pylab import *

h = [4,3,2,1]
x = [1,2]
y = np.convolve(x,h)
x = linspace(1, 5, 5) # de 1 a 5 con 5  muestras

markerline, stemlines, baseline = stem(x, y, '-.') #stem que grafica 
setp(markerline, 'markerfacecolor', 'b')#diferentes estilos de marcador
setp(baseline, 'color','r', 'linewidth', 2)#diferentes estilos de línea

#etiquetas
xlabel("xlabel")
ylabel("ylabel")



print(y)
show()