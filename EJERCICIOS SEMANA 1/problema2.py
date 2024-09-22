print("¿Cuál fue el monto de su consumo en el restaurant?")
consumo = float(input())
print("¿Cuanto porcentaje de propina desea dejar?")
propina= float(input())
if propina==15:
   propina=float(0.15*consumo)
   print("Usted tuvo un consumo de "+"$"+ str(consumo))
   print("Dejo una propina de "+"$"+ str(propina))
   print("GRACIAS POR SU PREFERENCIA")
elif propina>15:
     propinamayora15=float(propina/100)
     propina=float(propinamayora15*consumo)
     print("Usted tuvo un consumo de "+"$"+ str(consumo))
     print("Dejo una propina de "+"$"+ str(propina))
     print("GRACIAS POR SU PREFERENCIA")
else :
     print("Usted no consumio en nuestro restaurant,nuestros clientes dejan el 15% o más en propinas.")
