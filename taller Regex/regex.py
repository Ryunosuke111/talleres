import re

#PUNTO 1

#robert 'dot' colautti 'en' queensu 'dot' ca
#chris.eckert [at] queensu.ca
#lonnie.aarssen en queensu.ca

cadena1 = "robert 'dot' colautti 'at' queensu 'dot' ca"

'''Filtros Puntos'''

m1 = re.sub(" 'dot' ", ".",cadena1)
m2 = re.sub(" 'at' ","@",m1)

print(m2)

cadena2 = "chris.eckert[at]queensu.ca"
m3 = re.sub("\[at]","@",cadena2)

print(m3)

cadena3 = "lonnie.aarssen at queensu.ca"
m4 = re.sub(" at ","@",cadena3)

print(m4)
