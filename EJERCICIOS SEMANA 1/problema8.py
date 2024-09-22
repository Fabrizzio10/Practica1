print("Escriba la hora desde las 1:00 a 24:00")
time=input("hora: ")
hours,minutes=time.split(":")
horas_en_decimal= float(hours)+ float(minutes)
if horas_en_decimal>=7 and horas_en_decimal<=8:
   print("Hora del desayuno")
elif horas_en_decimal>=12 and horas_en_decimal<=13:
   print("Hora del almuerzo")
elif horas_en_decimal>=18 and horas_en_decimal<=19:
   print("Hora de la cena")
