#ejercicio temperatura de bodega
print("temperatura de la bodega".center(50).upper())

temp = int(input("ingrese la cantidad de temperaturas que desea ingresar (°C): "))
acumulador_temp = 0
contador_temp = 0
for i in range(1,temp + 1):
    dato_de_temp = float(input(f"ingrese la temperatura {i}: "))
    acumulador_temp += dato_de_temp
    contador_temp += 1
    promedio = acumulador_temp / contador_temp
    
if promedio < 15:
    print("ALERTA!!! Temperatura menor a 15°C")
elif promedio > 30:
    print("ALERTA!!! Temperatura mayor a 30°C")
else:
    print("temperatura segura")
print("el promedio es de {:.1f}".format(promedio))

#ejercicio de HCE:
HC = list()
contador_pacientes = 0
for x in range(1123):
  print("ingrese datos del nuevo paciente".center(50))
  name = input("ingrese nombre y un apellido: ")
  iden = input("ingrese documento: ")
  edad = input("ingrese edad: " )
  EPS = input("ingrese la eps: ")
  paciente = [name,iden,edad,EPS]
  HC.append(paciente)
  contador_pacientes += 1

  opt = int(input("""¿desea ingresar un nuevo paciente?
  \r1-si
  \r2-no\n"""))
  if opt == 1:
    continue
  else:
    print("adios\n")
    break
for y in HC:
  print("nombre del paciente: ", y[0])
  print("documento del paciente: ", y[1])
  print("edad del paciente: ", y[2])
  print("eps del paciente: ", y[3])
print("\nfin del programa")
