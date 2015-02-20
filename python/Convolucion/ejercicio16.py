"""
 conv x*x*x con x(n) = 1 para n=0,2,3,4,...30
"""
from pylab import *
x1=[]
for i in range(1,31):
    x1.append(1)
x2 = x1
x3 = x2
y = np.convolve(x1,x2)
z = np.convolve(y,x2)

n = linspace(1, len(x1)+len(x2)+ len(x3)-2, len(x1)+len(x2)+ len(x3)-2) 

markerline, stemlines, baseline = stem(n, z, '-.') #stem grafica 
setp(markerline, 'markerfacecolor', 'b')#diferentes estilos de marcador
setp(baseline, 'color','r', 'linewidth', 2)#diferentes estilos de línea

#etiquetas
xlabel("xlabel")
ylabel("ylabel")



print(z)
show()