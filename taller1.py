import numpy as np 
from matplotlib import pyplot as plt 
a = np.array([23,20,22,28,21,25,25,24])

print("datos de edad")
print (a)

print("datos de edad")
print (np.ptp(a))

print("cuartiles")

print (np.percentile(a, 25,))
print (np.percentile(a, 50,))
print (np.percentile(a, 75,))
print (np.percentile(a, 100,))

print("mediana")
print (np.median(a))

print("media")
print (np.mean(a))

print("desviacion estandar")
print (np.std(a))


x = [23,20,22,28,21,25,25,24]
y = [1,1,1,1,1,2,1,1]  

plt.bar(x, y, align = 'center') 
plt.title('Bar graph') 
plt.ylabel('cantidad') 
plt.xlabel('edad')
plt.show()