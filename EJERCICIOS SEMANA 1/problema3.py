#Creando Problema
#La juguetería "Mi Gabrielito" desea saber cuanto les cobrará la empresa de logística por payaso y muñeca que serán enviadas por correo
#Actualmente la juguetería hace envios por correo en dos ciudades: Trujillo y Chimbote
#La ciudad de Trujillo en el ultimo mes, demanda 23 payasos y 45 muñecas, mientras que Chimbote demanda 34 y 15 respectivamente.

Demanda_de_payasos_en_la_ciudad=int(input("Introducir demanda de payasos: "))
Demanda_de_muñecas_en_la_ciudad = int(input("Introducir demanda de muñecas: "))
print(f"LA DEMANDA TOTAL DE AMBOS PRODUCTOS EN ESTA CIUDAD ES: {Demanda_de_payasos_en_la_ciudad+Demanda_de_muñecas_en_la_ciudad}")
peso_payaso_en_kg = 0.112
peso_muñeca_en_kg = 0.075
print(f"El peso de los payasos enviados por correo a la ciudad son: {peso_payaso_en_kg*float(Demanda_de_payasos_en_la_ciudad)} kg")
print(f"El peso de las muñecas enviadas por correo a la ciudad son: {peso_muñeca_en_kg*float(Demanda_de_muñecas_en_la_ciudad)} kg")
a=peso_payaso_en_kg*float(Demanda_de_payasos_en_la_ciudad)
b=peso_muñeca_en_kg*float(Demanda_de_muñecas_en_la_ciudad)
print(f"El peso total del paquete de ambos productos enviado es: {a+b} kg")
