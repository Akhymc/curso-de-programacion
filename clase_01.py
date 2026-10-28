print("REPORTE PRESUPUESTARIO")
print("-----------------------")

proyecto = str(input("Ingrese el nombre del proyecto: "))

try:
    presupuesto = float(input("Ingrese el presupuesto: "))
    ejecutado = float(input("Ingrese el monto ejecutado: "))

    if presupuesto <= 0:
        print("El presupuesto debe ser mayor a 0")
    elif ejecutado < -1:
        print("El monto ejecutado debe ser mayor a 0")
    else:
        print("Datos ingresados correctamente")

except ValueError:
    print("Datos ingresados no validos")

print("Presupuesto: ",presupuesto)
print("Monto ejecutado: ",ejecutado)

print("                             ")

print("CALCULO DE SALDO DISPONIBLE")
print("----------------------------")

saldo = presupuesto - ejecutado
porcentaje = (ejecutado / presupuesto) * 100

print("Saldo disponible: ",saldo)
print("Porcentaje ejecutado: ", porcentaje, "%")

if porcentaje >= 80:
    print("Ejecucion alta")
elif porcentaje >= 50:
    print("Ejecucion media")
else:
    print("Ejecucion baja")


