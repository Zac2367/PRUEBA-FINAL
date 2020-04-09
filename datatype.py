# c es una cadena
c = "HOLA MUNDO"
print(c[::-1])
print(c.lower())

# y es un entero
y = (5,2)
print(y)
#podemos comprobarlo con la funcion type
print(type(c))
print(type(y))

print('{0:^8} | {1:^8} | {2:^8}'.format('Left','Center','Right'))
print('{0:^8} | {1:^8} | {2:^7}'.format(11,22,75))

l= [23,True,"HOLA MUNDO",[2,7]]
print(l[3][1])

mi_var=l[1:]
print(mi_var)

mi_var=l[:4]
print(mi_var)


x= [23,True,"HOLA MUNDO",[2,7]]
x[:]=[5,False,"adios",[1,9]]
print(x)

fav=False
if fav==True:
    print("\nMUY BIEN HECHO\t NO TE RINDAS")
else:
    print("\nSUERTE PARA LA PROXIMA")

num=7
if num==0:
    print("CERO")
elif num>0:
    print("POSITIVO")
elif num<0:
    print("NEGATIVO")

var= "PAR" if (num%2==0) else "IMPAR"
print(var)

edad = 0
while edad<18:
    edad+=1
    print("FELICIDADES TIENES " + str(edad) + " AÑOS\n")
    
