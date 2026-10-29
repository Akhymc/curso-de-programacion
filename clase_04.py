print("REPORTE PRESUPUESTARIO")
print("----------------------")

#SOLICITA EL NOMBRE DEL PROYECTO
proyecto = input("Ingrese el nombre del proyecto: ")

#BUCLE DE SOLICITUD DE PRESUPUESTO
while True:
    try:
        presupuesto = float(input("Ingrese el presupuesto: "))

        if presupuesto <= 0:
            print("El presupuesto debe ser mayor a cero")
            continue

        print ("Presupuesto Ingresado: ",presupuesto)
        break
    
    except ValueError:
        print("Error: Ingrese un numero valido")

#BUCLE DE SOLICITUD DE MONTO EJECUTADO
while True:
    try:
        ejecutado = float(input("Ingrese el monto ejecutado: "))

        if ejecutado < 0:
            print("El monto debe ser mayor a cero")
            continue

        print("Monto ejecutado ingresado: ",ejecutado)
        print("                                       ")
        print("*Datos ingresados correctamente, se procederá a realizar los calculos*")
        break

    except ValueError:
        print("Ingrese un dato valido")

#CALCULOS
print("Nombre del proyecto: ",proyecto)
saldo = presupuesto - ejecutado
print("Saldo disponible: ",saldo)
porcentaje = (ejecutado / presupuesto) * 100
print("Porcentaje ejecutado: ",porcentaje, "%")

if porcentaje >= 80:
    print("Ejecucion alta")
elif porcentaje >= 50:
    print("Ejecucion media")
else:
    print("Ejecucion baja")

#SOBREJECUCION
if ejecutado > presupuesto:
    print("ADVERTENCIA: Se ha superado el presupuesto")




