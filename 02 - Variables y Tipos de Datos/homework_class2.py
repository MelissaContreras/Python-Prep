import math
#1
x=8
print(x)

#2
CONSTANTE=8.5
print(type(CONSTANTE))

#3
print(type(x))

#4
mi_nombre="Melissa"

#5
numero_complejo=4+5j

#6
print(type(numero_complejo))

#7
pi_redondeado=round(math.pi,4)

#8 la primera es string y la otra booleano
a="True"
b=True
if a==b:
    print("son iguales")
else:
    print("no son iguales")
#9
print(type(a))
print(type(b))

#10
suma=6+2.4

#11
numero_complejo1=6+5j
numero_complejo2=8+3j
suma_complejos=numero_complejo1+numero_complejo2

#12
numero_real=7.2
numero_complejo3=8j
resultado=numero_real+numero_complejo3

#13
operacion= 5*3

#14
print(2**8)

#15
cociente=27/4
print(cociente)

#16
cociente2=27//4
print(cociente2)

#17
resto=27%4
print(resto)

#18
solucion=int(cociente)*4 +resto
print(solucion)

#19
t="hey"
w="13"
resultado_alfanumerico= t+w
print(resultado_alfanumerico)

#20
p="2"
u=2
if p==u:
    print("son iguales")
else:
    print("no son iguales")

#21
if p==str(u):
    print("son iguales")
else:
    print("no son iguales")

#22 debe usarse. en lugar de ,
#a = float('3,8')

#23
v=3
v-=1
print(v)

#24 uno en binario es 0b1
#al desplazar dos casilleros hacia a la izquierda da 0b100
#al traducir 0b100 nos da 4
# el sistema binario es el sistema que solo usa 2 numeros que son 0 y 1
1<<2
print(bin(1))
print(bin(1<<2))
print(1<<2)

#25 esta operacion de suma no esta permitida porque no son el mismo tipo de dato.
#print(2+"2")
"""
¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo
resultado?
No, porque si ambos fueran string podría concatenarlos.
o sí fueran int los sumaría.
"""

#26
mi_edad=29
mensaje="mi edad es "
print(mensaje+ str(mi_edad))

