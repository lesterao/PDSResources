"""
conv h*x
"""
from pylab import *

h = [3, 4.2 ,11, 7, -1, 0 , 2]
x = [1.2 , 3 , 0 , -0.5, 2]
y = np.convolve(x,h)
n = linspace(1,  len(h)+len(x)-1,  len(h)+len(x)-1) 

markerline, stemlines, baseline = stem(n, y, '-.') #stem que grafica 
setp(markerline, 'markerfacecolor', 'b')#diferentes estilos de marcador
setp(baseline, 'color','r', 'linewidth', 2)#diferentes estilos de línea

#etiquetas
xlabel("xlabel")
ylabel("ylabel")



print(y)
show()