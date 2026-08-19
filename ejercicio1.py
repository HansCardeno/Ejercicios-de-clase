# ejercicios de escritura condicionales
#1
A = int(input("ingrese un valor numerico para A: "))
B = int(input("ingrese un valor numerico para B: "))
if A > B:
    print(f"el valor A= {A} es mayor que B= {B}")
elif A < B:
    print(f"el valor A= {A} es menor que B= {B}")
elif A == B:
    print("ambos valores son iguales")

#2
print("ingrese el valor de sus notas con valores del 1 al 5")

A = float(input("ingrese la nota n°1: "))
B = float(input("ingrese la nota n°2: "))
C = float(input("ingrese la nota n°3: "))
D = float(input("ingrese la nota n°4: "))
E = float(input("ingrese la nota n°5: "))

per1 = .30
per2 = .15
per3 = .15
per4 = .20
per5 = .20

promedio = (A * per1) + (B * per2) + (C * per3) + (D * per4) + (E * per5)
if promedio >= 3.0:
    print("aprobado")

print(f"su promedio es de {promedio:.2f}")

#3
Y = float(input("ingrese un valor numerico para Y: "))
Z = float(input("ingrese un valor numerico para Z: "))
X = 0
if Y > Z:
    X=1

elif Y == Z:
    X=2

else:
    X=3

print(f"el valor de X es: {X}")

#4
print("ingrese valores numericos enteros diferentes para A, B y C")
A = int(input("ingrese un valor para A: "))
B = int(input("ingrese un valor para B: "))
C = int(input("ingrese un valor para C: "))

if A > B and A > C:
    if B > C:
        print(f"El orden descendente es: {A}, {B}, {C}.")
    else:
        print(f"El orden descendente es: {A}, {C}, {B}.")

elif B > A and B > C:
    if A > C:
        print(f"El orden descendente es: {B}, {A}, {C}.")
    else:
        print(f"El orden descendente es: {B}, {C}, {A}.")

else:
    if A > B:
        print(f"El orden descendente es: {C}, {A}, {B}.")
    else:
        print(f"El orden descendente es: {C}, {B}, {A}.")

#5
print("Para liquidar el pago de su matricula ingrese los siguientes datos:")

a = int(input("ingrese su número de inscripción: "))
b = input("ingrese su nombre completo: ")
c = float(input("ingrese su patrimonio: "))
d = int(input("ingrese su estrato: "))

constante_matricula = 50000
pat = .03

if c > 2000000 and d > 3:
    incremento = c * pat
    constante_matricula += incremento


print(f"número de inscripcion: {a}")
print(f"nombre completo: {b}")
print(f"su pago de matricula es de: {constante_matricula:.2f}")
