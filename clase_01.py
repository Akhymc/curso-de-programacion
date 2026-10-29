print("REPORTE PRESUPUESTARIO")
print("-----------------------")

proyecto = str(input("Ingrese el nombre del proyecto: "))

try:
    presupuesto = float(input("Ingrese el presupuesto: "))
    ejecutado = float(input("Ingrese el monto ejecutado: "))

    if presupuesto <= 0:
        print("Error: el presupuesto debe ser mayor que 0")
    elif ejecutado < 0:
        print("Error: el monto ejecutado no puede ser negativo")
    else:
        print("Datos ingresados correctamente")
        print("                               ")
        print("Proyecto: ",proyecto)
        print("Presupuesto: ",presupuesto)
        print("Monto ejecutado: ",ejecutado)

        print("---------------------------")
        print("CALCULO DE SALDO DISPONIBLE")
        print("----------------------------")

        #CALCULOS

        saldo = presupuesto - ejecutado
        porcentaje = (ejecutado / presupuesto) * 100

        print("Saldo disponible: ", saldo)
        print("Porcentaje ejecutado: ",porcentaje, "%")

        #CLASIFICACION
        
        if porcentaje >= 80:
            print("Ejecucion alta")
        elif porcentaje >= 50:
            print("Ejecucion media")
        else:
            print("Ejecucion baja")

        #SOBREEJECUCION

        if ejecutado > presupuesto:
            print("ADVERTENCIA: Se ha superado el presupuesto")
except ValueError:
    print("Error: debe ingresar valores numericos validos")
   
