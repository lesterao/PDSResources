"""
h(n)= e^(-0.15n) para n=0,1,2,...32; x(n)= 1 para n=0,1,2,...20
"""
from pylab import *
h1=[]
u1=[]
for i in range(1,33): # 32 muestras
    h1.append(exp(-0.15*(i-1)))

for i in range(1,21): # 20 muestras
    u1.append(1)

z = np.convolve(u1,h1)
n = linspace(1, len(h1)+len(u1)-1, len(h1)+len(u1)-1) 

markerline, stemlines, baseline = stem(n, z, '-.') #stem grafica 
setp(markerline, 'markerfacecolor', 'b')#diferentes estilos de marcador
setp(baseline, 'color','r', 'linewidth', 2)#diferentes estilos de línea

#etiquetas
xlabel("xlabel")
ylabel("ylabel")



print(z)
show()
