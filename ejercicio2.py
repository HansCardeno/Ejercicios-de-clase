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
