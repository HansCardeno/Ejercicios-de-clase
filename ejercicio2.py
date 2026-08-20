# ejercicio de estructura secuencial
#1
A = int(input("ingrese un número: "))

print(f"el cuadrado del número es: {A**2}")
print(f"el cubo del número es: {A**3}")

#2
emp1 = .1
emp2 = .12
emp3 = .15

Sueldo = float(input("ingrese su sueldo: "))
print("el nuevo salario con el 10% de aumento es: {}".format(Sueldo + Sueldo * emp1))
print("el nuevo salario con el 12% de aumento es: {}".format(Sueldo + Sueldo * emp2))
print("el nuevo salario con el 15% de aumento es: {}".format(Sueldo + Sueldo * emp3))

#3 (4)
print("para calcular el area y perimetro de una circunferencia, ingrese los valores pedidos: ")

Radio = float(input("ingrese un valor para el radio de la circunferencia: "))
pi = 3.1416
Area_circunferencia = pi * (Radio ** 2)
Perimetro_circunferencia = 2 * pi * Radio
print("el área de la circunferencia es: {}".format(Area_circunferencia))
print("el perímetro de la circunferencia es: {}".format(Perimetro_circunferencia))

#4 (5)
pasos = int(input("ingrese el número de pasos que ha dado: "))
distancia_cm = 45
dt_cm = distancia_cm * pasos
dt_m = dt_cm / 100
dt_km = dt_m / 1000

print(f"la distancia recorrida en centimetros es: {dt_cm:.3f} cm")
print(f"la distancia recorrida en metros es: {dt_m:.3f} m")
print(f"la distancia recorrida en kilometros es: {dt_km:.3f} km")

#5 (6)
print("conversor de grados a radianes")
grados = float(input("ingrese los grados: "))
rad = grados * (3.1416 / 180)

print(f"el valor en radianes de {grados}° es: {rad:.3f} rad")

#6 (7)
celcius = float(input("ingrese la temperatura en grados celsius: "))
kelvin = celcius + 273.15
fahrenheit = (celcius * 9/5) + 32

print(f"temperatura en grados celcius es: {celcius:.1f}°")
print(f"temperatura en grados kelvin es: {kelvin:.1f}°")
print(f"temperatura en grados fahrenheit es: {fahrenheit:.1f}°")

#ejercicios ciclos
#1
num1 = int(input("Ingresa el primer entero: "))
num2 = int(input("Ingresa el segundo entero: "))
resultado = 0

for i in range(num2):
    resultado += num1

print(f"El resultado de la multiplicación es: {resultado}")

#2
notas = int(input("ingrese su numero de notas: "))
suma_n = 0

for i in range(notas):
    nota = float(input(f"Ingrese la nota {i + 1} (de 0 a 5): "))
    suma_n += nota

promedio = suma_n / notas

print(f"El promedio de la materia es: {promedio}")

#3
print("utilice solo numeros enteros positivos de maximo valor 9")
N = int(input("Ingrese un valor para n (máximo 9): "))
X = int(input("Ingrese un valor para x (máximo 9): "))

for i in range(N + 1):
    resultado = i ** X
    print(f"{i}^{X} = {resultado}")

#4
N = int(input("Ingrese el valor límite N: "))
suma_impar = 0

for i in range(1, N + 1):
    if i % 2 != 0:
        suma_impar += i

print(f"La suma de los números impares es: {suma_impar}")

#5
while True:
    numero = int(input("Ingrese un número entero entre 0 y 20: "))
    
    if numero < 0 or numero > 20:
        print("porfavor, ingrese un número entre 0 y 20.")
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es:{factorial}")
    
    opt = input("¿Desea volver a empezar? (s/n): ")
    if opt.lower() != 's':
        break

#6
a = float(input("Ingrese un valor para a: "))
n = int(input("Ingrese el número de términos n: "))
sumatoria = 0.0

for i in range(1, n + 1):
    termino = (1 / a) ** i
    sumatoria += termino

print(f"El resultado de la sumatoria es: {sumatoria}")
